# SatchelTwo CLI Mainscript
# Take control of your homework!
# ProjectSCR 2026

#Setting up libraries

import subprocess
import os
import sys

#Variables

buildVersion = "PRE-DVT Milestone 1"

#Defining main menu function

def mainmenu():
    print("Main menu:")
    print("1. Assignments")
    print("2. Refresh Calendar / Setup Account")
    print("3. About")
    print("4. Exit")
    menuSelect = int(input("Please type the corresponding number for your option choice: "))
    if menuSelect == 4:
        exit()
    elif menuSelect == 2:
        os.system("python3 fetch.py")
    elif menuSelect == 1:
        os.system("python3 assignments.py")
    elif menuSelect == 3:
        about()
    else:
        print("That is not a valid option!")
        mainmenu()

# Defining the About function

def about():
    platformVersion = sys.platform()
    print("SatchelTwo CLI")
    print(buildVersion)
    print("Currently running on platform: ", platformVersion)
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