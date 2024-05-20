# Author: Arabian Coconut
# Date modified: 21-May-2024
# Desc: This is a small program to open WhatsApp links on WhatsApp web/desktop

import requests
import webbrowser


def whatsapp_app_link(data):
    url = f"https://api.whatsapp.com/send/?phone={data}&app_absent=0"
    r = requests.get(url)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 404:
        print("Diagnostics: Page not found")
    else:
        print("Diagnostics: Error Occurred")
