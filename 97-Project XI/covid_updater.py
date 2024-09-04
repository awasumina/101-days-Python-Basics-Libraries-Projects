# pip install requests, win10toast
# reuests library allows us to send requests to different websites
# win10toast allows us to show notificitaion in windows

import requests
from win10toast import ToastNotifier
import json # An API which allows us the as to be in json format
import time

def update():
    
    r = requests.get('https://api.covid19api.com/all')
    r.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
    data = r.json() # convert data into json format
    # text = f'Confirmed Cases: {data["cases"]}\nDeaths: {data["deaths"]}\nRecovered: {data["recovered"]}'
    text = f'Confirmed Cases: {data["cases"]}\nDeaths: {data["deaths"]}\nRecovered: {data["recovered"]}'

    while True :
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration = 20) #sleep after 20 seconds
        time.sleep(60) #every 60 minute this notification will pop up again


update()


# ============================================

# import requests
# from win10toast import ToastNotifier
# import time

# def update():
#     while True:
#         # try:
#             r = requests.get('https://coronavirus.jhu.edu/map.html') 
#             data = r.json()
#             text = f'Confirmed Cases: {data["cases"]}\nDeaths: {data["deaths"]}\nRecovered: {data["recovered"]}'
#             toast = ToastNotifier()
#             toast.show_toast("Covid-19 Updates", text, duration=20)
#             time.sleep(3600)  # Show the notification every 60 minutes
            
#         # except Exception as e:
#         #     print(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     update()
