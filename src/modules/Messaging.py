# Author : Arabian Coconut
# Date   : 01-09-2023
# Desc   : This is a small program to open whatsapp links in whatsapp web/desktop

import requests
import webbrowser


def whatsapp_app_link(data):
    phone_number = data
    url = f"https://api.whatsapp.com/send/?phone={phone_number}&app_absent=0"
    r = requests.get(url)
    if r.status_code == 200:
        webbrowser.open(url)
    elif r.status_code == 404:
        print("Diagnostics: Page not found")
    else:
        print("Diagnostics: Error Occurred")
