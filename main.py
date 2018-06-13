import requests
#https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=YOUR_API_KEY

from keys import GOOGLEAPIKEY
from const import DIRECTIONURL

locationstart='2 windsock close london se16 7fl'
locationend='Manchester'
locationstart = locationstart.replace(' ','+')

DIRECTIONURL = DIRECTIONURL+"?origin="+locationstart+"&destination="+locationend+"&"+GOOGLEAPIKEY
html_steps = ''

print(DIRECTIONURL)


response = requests.get(DIRECTIONURL)

if response.ok:
    print('ok')
    data = response.json()
    for step in (data['routes'][0]['legs'][0]['steps']):
        html_steps = html_steps+(step['html_instructions'])

#with open('animals.txt', 'w') as f:
#    for animal in animals:
#        f.write(animal + "\n")

with open('direction.html','w') as file:
    file.write(html_steps)

 ##print(data['html_instructions'])
