# SatchelTwo CLI Fetcher
# A command line based tool for importing SatchelOne calendars into spreadsheets
# ProjectSCR 2026

#Lots of library setup

from icalendar import Calendar
import csv
import urllib.request
import shutil
import sys
import os
import ssl
from datetime import datetime, date
import webbrowser
import time
import pandas as pd

#Setting up an SSL HTTPS context so it doesn't throw security errors

ssl._create_default_https_context = ssl._create_unverified_context

#Variables for configuring directories

downloadlocation = 0
calendarlocation = 0
downloadfolder = 0
configlocation = 0

#Checks for a config file to avoid the user always inputting a calendar api url

def checkConfig():
    if os.path.exists(configlocation) == False:
        config = open(configlocation, "w")
        url = "https://www.satchelone.com/sync-calendar"
        print("Press the 'Copy URL' button on the page that opens!")
        time.sleep(3)
        webbrowser.open(url, new=0, autoraise=True)
        config.write(input("Paste URL here: "))
        config.close()
        config = open(configlocation, "r")
        satchellink = config.read()
        config.close()
        return satchellink
    else:
        config = open(configlocation, "r")
        satchellink = config.read()
        config.close()
        return satchellink

#Setting directories for specific platforms (Linux and MacOS share the same file structure so they're grouped together)

if sys.platform == "win32":
    os.system("mkdir %APPDATA%/Local/SatchelTwo/")
    os.system("mkdir %APPDATA%/Local/SatchelTwo/Download/")
    downloadlocation = "%APPDATA%/Local/SatchelTwo/Download/icalendars.ics"
    calendarlocation = "%APPDATA%/Local/SatchelTwo/Download/icalendars.csv"
    downloadfolder = "%APPDATA%/Local/SatchelTwo/Download/"
    configlocation = "%APPDATA%/Local/SatchelTwo/config.txt"
elif sys.platform == "darwin" or "linux":
    os.system("mkdir ~/SatchelTwo/")
    os.system("mkdir ~/SatchelTwo/Download/")
    downloadlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.ics")
    calendarlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.csv")
    downloadfolder = os.path.expanduser("~/SatchelTwo/Download/")
    configlocation = os.path.expanduser("~/SatchelTwo/config.txt")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!") #Throwing an error for those who try running SatchelTwo on their... idk... Wii U?

#Running the check config function to get the api url then downloading that

satchellink = checkConfig()
destination = downloadlocation
print("Downloading ICAL")
urllib.request.urlretrieve(satchellink, destination)

#Preparing the ics to csv conversion

filename = downloadlocation
file_extension = str("ics")
headers = ('Summary', 'UID', 'Description', 'Location', 'Start Time', 'End Time', 'URL')

#Object oriented to make things cleaner down the line

class CalendarEvent:
    """Calendar event class"""
    summary = ''
    uid = ''
    description = ''
    location = ''
    start = ''
    end = ''
    url = ''

    def __init__(self, name):
        self.name = name

events = []

# The big chunk of the script that reads the ical

def open_cal():
    if os.path.isfile(filename):
        if file_extension == 'ics':
            f = open(downloadlocation, 'rb')
            gcal = Calendar.from_ical(f.read())

            for component in gcal.walk():
                event = CalendarEvent("event")
                if component.get('TRANSP') == 'TRANSPARENT': continue #skip event that have not been accepted
                if component.get('SUMMARY') == None: continue #skip blank items
                event.summary = component.get('SUMMARY')
                event.uid = component.get('UID')
                if component.get('DESCRIPTION') == None: continue #skip blank items
                event.description = component.get('DESCRIPTION')
                event.location = component.get('LOCATION')
                if hasattr(component.get('dtstart'), 'dt'):
                    event.start = component.get('dtstart').dt
                    if isinstance(event.start, date):
                        event.start = datetime.combine(event.start, datetime.min.time())
                if hasattr(component.get('dtend'), 'dt'):
                    event.end = component.get('dtend').dt
                    if isinstance(event.end, date):
                        event.end = datetime.combine(event.end, datetime.min.time())


                event.url = component.get('URL')
                events.append(event)
            f.close()
        else:
            print("You entered ", filename, ". ")
            print(file_extension.upper(), " is not a valid file format. Looking for an ICS file.")
            exit(0)
    else:
        print("I can't find the file ", filename, ".")
        print("Please enter an ics file located in the same folder as this script.")
        exit(0)

# Writing the ical data to the CSV

def csv_write(icsfile):
    csvfile = icsfile[:-3] + "csv"
    try:
        with open(csvfile, 'w') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(headers)
            for event in sortedevents:
                values = (event.summary.encode('utf8').decode(), event.uid, event.description.encode('utf8').decode(), event.location, event.start, event.end, event.url)
                wr.writerow(values)
    except IOError:
        print("Could not open file! Please close Excel!")
        exit(0)

open_cal() #Deprecated but runs anyways -\('_')/-
sortedevents=sorted(events, key=lambda obj: obj.start)
print("Writing CSV...")
csv_write(filename)

#Preparing to clean the CSV

input_csv = calendarlocation
output_csv = (downloadfolder + "/cleaned.csv")

df = pd.read_csv(input_csv)

# Prepare new columns
new_columns = [
    "Name",
    "Class Name",
    "Homework Title",
    "Set By",
    "Set On",
    "Due On"
]

for col in new_columns:
    df[col] = None

# Parsing the whole thing to remove the leftover newlines from ical format

def parse_description(desc):
    if pd.isna(desc):
        return [None] * 6

    # Normalize newlines and split
    parts = (
        desc.replace("\\n", "\n")
            .replace("\r\n", "\n")
            .split("\n")
    )

    # Pad or trim to exactly 6 elements
    parts = (parts + [None] * 6)[:6]

    cleaned = []
    for i, part in enumerate(parts):
        if part is None:
            cleaned.append(None)
        elif ":" in part and i != 0:
            cleaned.append(part.split(":", 1)[1].strip())
        else:
            cleaned.append(part.strip())

    return cleaned

# Apply parsing so it looks nice and tidy
df[new_columns] = df["Description"].apply(
    lambda x: pd.Series(parse_description(x))
)

# Dropping the original Description column
df = df.drop(columns=["Description"])

df.to_csv(output_csv, index=False)

print("Cleaning up CSV...")


print("Calendar has been setup!")
os.system("python3 main.py")