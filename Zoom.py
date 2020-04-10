import webbrowser
import time
import datetime


def openLink(url):
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
        "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(url)


def zoomJoin(h, m, url):
    for i in range(0, 365):
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, h, m)
        if t.hour >= 2:
            future += datetime.timedelta(days=1)
        time.sleep((future-t).seconds)
    openLink(url)


# Calling the Function
zoomJoin(h, m, Link)
# h = Hour in 24 format
# m = Minutes in 24 format
# Link = Paste the Zoom link in " " or ' '

"""
EXAMPLE:
zoomJoin(10, 00, "https://zoom.us/w/xxxxxxxxx")
"""
