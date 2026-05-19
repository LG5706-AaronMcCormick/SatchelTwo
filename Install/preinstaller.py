# Satchel:Two Installer script
# "I'm trying to make it cross-platform, I swear!" - Aaron McCormick, 2026

# Libraries, you know the drill..

import sys
import os
import platform
import time

# Setting up the dir's

projfile = os.path.realpath(__file__)
dir = os.path.dirname(projfile)

# Prepping the installer

print("Welcome to the Satchel:Two Pre-Installer!")
print("Please follow the guide at https://github.com/LG5706-AaronMcCormick/Satchel-Two/wiki/SatchelTwo-CLI#installing-the-cli")
print()
time.sleep(3)
print("STAGE 1: Running platform checks...")
print()

archOK = False
osOK = False
pyOK = False
systemOK = False

# Architecture check: amd64 and arm64 will pass, x86 will not
arch = platform.machine() # arm64, amd64, i386 ect
if arch != "arm64" and arch != "amd64":
    archOK = False
else:
    archOK = True

# OS Check: Doesn't really matter as long as it's 64-bit and runs Python 3.13.5
if sys.platform != "win32":
    if arch == "arm64" and sys.platform == "win32":
        osOK = False
        archOK = False
    else:
        if sys.platform != "darwin":
            if sys.platform != "linux":
                osOK = True
            else:
                osOK = True
        else:
            osOK = False
else:
    osOK = True

# Python version check: Checks to see if Python is 3.13.5 or newer
pyver = list(platform.python_version_tuple())
pyvermaj = int(pyver[0])
pyvermin = int(pyver[1])
pyverpch = int(pyver[2])
if pyvermaj >= 3:
    if pyvermin >= 13:
            pyOK = True
    else:
        pyOK = False
else:
    pyOK = False
pyver = (str(pyvermaj) + "." + str(pyvermin) + "." + str(pyverpch))



print("SYSTEM SUMMARY ================ ")
if pyOK == False:
    if osOK == False and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (FAILED) ")
        time.sleep(1)
    if osOK == True and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (FAILED) ")
        time.sleep(1)
    if osOK == True and archOK == True:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (PASSED) ")
        time.sleep(1)
        print("System Architecture", arch, " (PASSED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (FAILED) ")
        time.sleep(1)
if pyOK == True:
    if osOK == False and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (PASSED) ")
        time.sleep(1)
    if osOK == True and archOK == False:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (FAILED) ")
        time.sleep(1)
        print("System Architecture", arch, " (FAILED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (PASSED) ")
        time.sleep(1)
    if osOK == True and archOK == True:
        time.sleep(1)
        print("Operating System: ", sys.platform, " (PASSED) ")
        time.sleep(1)
        print("System Architecture", arch, " (PASSED) ")
        time.sleep(1)
        print("Python Version:", pyver, " (PASSED) ")
        time.sleep(1)
        systemOK = True
print()

if systemOK == True:
    print("Your system has passed the initial tests and can continue to the second step of installation.")
    time.sleep(1)
    if sys.platform == "darwin" or "linux":
        print("However, MacOS and Linux systems will install the required libraries using --break-system-packages.")
        print("This hasn't been reported to be an issue, but this is a very subtle warning!")
else:
    print("Your system has failed the tests above. The installation cannot continue.")
    exit()

print()
passed1 = str(input("Would you like to continue? Y/N : "))
if passed1 != "Y":
    print("Installation aborted manually.")
    exit()

print()
print("STAGE 2: Installing Libraries...")

try: 
    os.system("pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r" + dir + "/requirements.txt")

except Exception as e:
    print("This error occured while installing libraries:", e)
    print("Installation aborted.")
    exit()

print("")
print("Library install complete!")
print("Satchel:Two is now ready to install!")