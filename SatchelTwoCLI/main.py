# SatchelTwo CLI Mainscript
# Take control of your homework!
# ProjectSCR 2026

#Setting up libraries

import subprocess
import os
import sys
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')  # Suppress all warnings

#Variables

buildVersion = "Milestone 1.2"

#Defining main menu function

def mainmenu():
    print("Main menu:")
    print("1. Assignments")
    print("2. Refresh Calendar / Setup Account")
    print("3. About")
    print("4. Token Setup (BETA)")
    print("5. Exit")
    menuSelect = int(input("Please type the corresponding number for your option choice: "))
    if menuSelect == 4:
        if sys.platform == "win32":
            os.system("python tokensetup.py")
        else:
            os.system("python3 tokensetup.py")
    elif menuSelect == 2:
        if sys.platform == "win32":
            os.system("python fetch.py")
        else:
            os.system("python3 fetch.py")
    elif menuSelect == 1:
        if sys.platform == "win32":
            os.system("python assignments.py")
        else:
            os.system("python3 assignments.py")
    elif menuSelect == 3:
        about()
    elif menuSelect == 5:
        exit()
    else:
        print("That is not a valid option!")
        mainmenu()

# Defining the About function

def about():
    print(r"  _________       __         .__           ._____________              ")
    print(r" /   _____/____ _/  |_  ____ |  |__   ____ |  \__    ___/_  _  ______  ")
    print(r" \_____  \\__  \\   __\/ ___\|  |  \_/ __ \|  | |    |  \ \/ \/ /  _ \ ")
    print(r" /        \/ __ \|  | \  \___|   Y  \  ___/|  |_|    |   \     (  <_> )")
    print(r"/_______/ (____  /__|  \___  >___|  /\___  >____/____|    \/\_/ \____/ ")
    platformVersion = sys.platform
    print("")
    print("SatchelTwo CLI")
    print(buildVersion)
    print("Currently running on platform: ", platformVersion)
    print("")
    mainmenu()

#Checking for internet connectivity on startup

result = subprocess.run(
    ["ping", "-c", "1", "8.8.8.8"] if subprocess.os.name != "nt" else ["ping", "-n", "1", "8.8.8.8"], #Pinging Google's DNS
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

if result.returncode == 0: #If no packets return,
    print("")
else:
    raise Exception("EXCEPTION OCCURED: Connection failed! Please check your internet connectivity!") #Raise an exception

mainmenu()