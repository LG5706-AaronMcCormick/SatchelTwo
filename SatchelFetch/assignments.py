# SatchelTwo CLI Assignments
# A command line tool for viewing assignments!
# ProjectSCR 2026

#Setting up libraries

import pandas as pd
import sys
import os

#Configuring Pandas to use the full width of the window

pd.set_option('display.max_colwidth', None)

#Initialising directories for different platforms

calendarlocation = 0

if sys.platform == "win32":
    calendarlocation = "%APPDATA%/Local/SatchelTwo/Download/cleaned.csv"
elif sys.platform == "darwin" or "linux":
    calendarlocation = os.path.expanduser("~/SatchelTwo/Download/cleaned.csv")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!")

#Checking for the calendar file

if os.path.exists(calendarlocation) == False:
    raise Exception("You have not setup your calendar token! Please return to the main script and select 'Setup Account'.")

#Printing the calendar to the screen and returning to the main menu

df = pd.read_csv(calendarlocation, usecols=["Class Name", "Homework Title", "Set By", "Set On", "Due On"])
print(df)
os.system("python3 main.py")