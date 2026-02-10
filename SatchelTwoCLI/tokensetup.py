# SatchelTwo CLI Token Setup
# For advanced users only who want to test experimental features

# Library setup 

import urllib.request
import shutil
import sys
import os
import ssl
from datetime import datetime, date
import webbrowser
import time
import pandas as pd
from pathlib import Path
import requests
import warnings

warnings.filterwarnings('ignore')  # Suppress all warnings

# Setting up an ssl context because it gets mad if you don't

ssl._create_default_https_context = ssl._create_unverified_context

#Variables for configuring directories

downloadlocation = 0
calendarlocation = 0
downloadfolder = 0
configlocation = 0

if sys.platform == "win32":
    home = Path.home()
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo"')
    os.system(r'mkdir "%userprofile%\Documents\SatchelTwo\Download"')
    downloadlocation = home / "Documents" / "SatchelTwo" / "Download" / "icalendars.ics"
    calendarlocation = home / "Documents" / "SatchelTwo" / "Download" / "icalendars.csv"
    cleanedlocation = home / "Documents" / "SatchelTwo" / "Download" / "cleaned.csv"
    downloadfolder = home / "Documents" / "SatchelTwo" / "Download"
    configlocation = home / "Documents" / "SatchelTwo" / "config.txt"
    tokenlocation = home / "Documents" / "SatchelTwo" / "token.txt"
elif sys.platform == "darwin" or sys.platform == "linux":
    os.system("mkdir ~/SatchelTwo/")
    os.system("mkdir ~/SatchelTwo/Download/")
    downloadlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.ics")
    calendarlocation = os.path.expanduser("~/SatchelTwo/Download/icalendars.csv")
    cleanedlocation = os.path.expanduser("~/SatchelTwo/Download/cleaned.csv")
    downloadfolder = os.path.expanduser("~/SatchelTwo/Download/")
    configlocation = os.path.expanduser("~/SatchelTwo/config.txt")
    tokenlocation = os.path.expanduser("~/SatchelTwo/token.txt")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!") #Throwing an error for those who try running SatchelTwo on some random device.

# Setting up a script to get and write the token to a text file

def checkToken():
    if os.path.exists(tokenlocation) == False:
        if sys.platform == "win32":
            home = Path.home()
            target_dir = home / "Documents" / "SatchelTwo"
            target_dir.mkdir(parents=True, exist_ok=True)
            file_path = target_dir / "token.txt"
            file_path.write_text("")    
        tokenfile = open(tokenlocation, "w")
        tokenfile.write(input("Paste your Student Token here: "))
        tokenfile.close()
        tokenfile = open(tokenlocation, "r")
        token = tokenfile.read()
        tokenfile.close()
        return token
    else:
        tokenfile = open(tokenlocation, "r")
        token = tokenfile.read()
        tokenfile.close()
        return token

# Displaying a warning before taking the user to the token setup page

accepted = input("Warning! This is for only advanced users and enables experimental features, do you want to continue? Y/N: ")
if accepted == "N":
    if sys.platform == "win32":
        os.system("python main.py")
    else:
        os.system("python3 main.py")

if os.path.exists(tokenlocation) == False:
    print("Redirecting to token setup page...")
    url = "https://github.com/LG5706-AaronMcCormick/SatchelTwo/blob/main/SatchelTwoCLI/TokenSetup.md"
    time.sleep(3)
    webbrowser.open(url, new=0, autoraise=True)

studenttoken = checkToken()

# Getting the user to input their own Authentication key as that should be kept securely!

auth = input("Please enter your authenication key (It should include an equals at the end!): ")

# Whole bunch of URL stuff to send for specific headers using the token and response

url = ("https://api.satchelone.com/api/students/" + studenttoken)
params = {
    "include": "user_private_info"
}

headers = {
    "Accept": "application/smhw.v2021.5+json",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.satchelone.com/todos/upcoming",
    "X-Platform": "web",
    "Authorization": ("Bearer" + auth ),
    "Origin": "https://www.satchelone.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "If-None-Match": 'W/"72d6b5ac5b8eec8c5f5ce2e0d1f5979a"',
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) "
        "Gecko/20100101 Firefox/147.0"
    ),
}

response = requests.get(url, headers=headers, params=params)

# Raise an exception for HTTP errors
response.raise_for_status()

# Parse the JSON response from the SatchelOne API
data = response.json()

# Get the headers, you know the rules. (AND SO DO I!)

response = requests.get(url, headers=headers, params=params)
response.raise_for_status()
data = response.json()

# Getting that info from the response JSON
upi = data.get("user_private_infos", [{}])[0]

email = upi.get("email")
username = upi.get("username")
uid = upi.get("uid")

print("Your email must be", email, "...")
print("And that means your username is", username, "...")
print("So your UserID is", uid, "!")
print("Token setup successful! Please make sure you save your authentication key!")

if sys.platform == "win32":
    os.system("python main.py")
else:
    os.system("python3 main.py")
