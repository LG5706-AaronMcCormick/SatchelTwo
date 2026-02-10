# Token Setup for SatchelAPI (BETA)

## BE AWARE THIS IS VERY COMPLEX AND REQUIRES A DESKTOP DEVICE.

This guide is for advanced users who would like to use some extended features of SatchelTwo by importing their token into the app. It's quite complicated to do, and the instructions are browser specific, so please follow the guide for your respective browser. With that out of the way, let's get right to it!

### Firefox

For Firefox, this is pretty simple. Well, to an extent.

1. First, open up Firefox and log into your SatchelOne account
2. Once on the landing page for Satchel (it should be the to-do list page) press:
- Windows and Linux: CTRL + Shift + I or F12
- MacOS: Command + Option + I
3. This should bring you to the web developer page.
4. Next, press "Network" on the toolbar and refresh the SatchelOne webpage. Your developer tools window should now be full of logged network communications!
5. Look for a GET from the domain "api.satchelone.com" and has a JSON file starting with a few numbers followed by a "?". This is where your token is.
6. Do a single left click on that and it should bring up a side panel. Look near the top of it for some text like: https://api.satchelone.com/api/students/...
7. In that URL, there should be some numbers after students, followed by a question mark.
8. Congratulations! This is your student token! Save it somewhere convenient so you can come back to it later!
9. Next, we need to get your authentication. Scroll down the side pane until you see "Request headers" and look for "Authentication:". It should have a value that ends in an equals symbol.
10. Copy that whole value (Including equals!) out of there and save it somewhere safe, preferably with your student token. This is your authentication key and will be neccesary to use the SatchelOneAPI.
11. Were all set! You now have the neccesary data to use the SatchelOne API!

### Google Chrome / Chromium

(Instructions coming soon as I do not use chrome and don't have it installed at the time of writing)
