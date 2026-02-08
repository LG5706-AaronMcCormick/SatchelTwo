# SatchelTwo CLI Assignments
# A command line tool for viewing assignments!
# ProjectSCR 2026

#Setting up libraries

import pandas as pd
import sys
import os
from pathlib import Path

#Configuring Pandas to use the full width of the window

pd.set_option('display.max_colwidth', None)

#Initialising directories for different platforms

if sys.platform == "win32":
    home = Path.home()

calendarlocation = 0

if sys.platform == "win32":
    calendarlocation = home / "Documents" / "SatchelTwo" / "Download" / "cleaned.csv"
elif sys.platform == "darwin" or "linux":
    calendarlocation = os.path.expanduser("~/SatchelTwo/Download/cleaned.csv")
else:
    raise Exception("Sorry, whatever obscure platform you're using is not supported!")

#Checking for the calendar file

if os.path.exists(calendarlocation) == False:
    raise Exception("You have not setup your calendar token! Please return to the main script and select 'Setup Account'.")

#Printing the calendar to the screen and returning to the main menu
# Again Win32 needs cp1252 so there has to be yet another condition here

if sys.platform == "win32":
    df = pd.read_csv(calendarlocation, encoding="cp1252", usecols=["Class Name", "Homework Title", "Set By", "Set On", "Due On"])
else:
    df = pd.read_csv(calendarlocation, usecols=["Class Name", "Homework Title", "Set By", "Set On", "Due On"])
print(df)
if sys.platform == "win32":
    os.system("python main.py")
else:
    os.system("python3 main.py")