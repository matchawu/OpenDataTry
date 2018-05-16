import requests
import time
from datetime import datetime  
from datetime import timedelta  


lat = 23.5
lng = 120
lat1 = str(lat)
lng1 = str(lng)
payload = {'lat': lat1 , 'lng': lng1 ,'date': 'today'}
r = requests.get('https://api.sunrise-sunset.org/json?', params=payload)
# print(r.text)
print("Your latitude is" + lat + ",and your longitude is"+ lng +".")
k = r.json()
# print(k['results']['status'])
print("====== This is original response using UTC ======")
print(k['results']['sunrise'])
print(k['results']['sunset'])

# dt = datetime.strptime("2015-07-08 11:20:28",'%Y-%m-%d %H:%M:%S')
dt1 = datetime.strptime(k['results']['sunrise'],'%H:%M:%S PM')
dt2 = datetime.strptime(k['results']['sunset'],'%H:%M:%S AM')
# print(dt1.strftime("%H:%M:%S"))
# print(dt2.strftime("%H:%M:%S"))
print("====== This is the one using UTC+8 ======")
dt1+=timedelta(hours=20)
dt2+=timedelta(hours=32)    
print("The sunrise time is at " + dt1.strftime("%H:%M:%S"))
print("The sunset time is at " + dt2.strftime("%H:%M:%S"))

# sunrise = k['results']['sunrise'] 
# sunset = k['results']['sunset'] 