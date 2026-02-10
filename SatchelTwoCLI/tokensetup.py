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

# Setting up an ssl context because it gets mad if you don't

ssl._create_default_https_context = ssl._create_unverified_context

#Variables for configuring directories

downloadlocation = 0
calendarlocation = 0
downloadfolder = 0
configlocation = 0

if sys.platform == "win32":
    home = Path.home()
    os.system('mkdir "%userprofile%\Documents\SatchelTwo"')
    os.system('mkdir "%userprofile%\Documents\SatchelTwo\Download"')
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

accepted = input("Warning! This is for only advanced users and enables experimental features, do you want to continue? Y/N: ")
if accepted == "N":
    if sys.platform == "win32":
        os.system("python main.py")
    else:
        os.system("python3 main.py")

print("Sorry! This feature is still under heavy construction! Please wait for a future update!")
exit()

print("Redirecting to token setup page...")
url = "https://github.com/LG5706-AaronMcCormick/SatchelTwo/blob/main/SatchelTwoCLI/TokenSetup.md"
time.sleep(3)
webbrowser.open(url, new=0, autoraise=True)

studenttoken = checkToken()
url = ('https://api.satchelone.com/api/students/' + studenttoken + '?include=user_private_info,school,package,premium_features')
x = requests.get(url)
print(x.headers)