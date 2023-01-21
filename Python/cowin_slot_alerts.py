import requests
import smtplib
import json
import time
import datetime


# define variable
MY_EMAIL = "me.ansh@gmail.com"
MY_PWD = "Gmail*9876#"
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date=15-05-2021"
response = requests.get()