import requests
q = requests.get("https://api.open-meteo.com/v1/forecast?latitude=55.7558&longitude=37.6176&current_weather=true")
wea = q.json()
curtemp = wea['current_weather']['temperature']
print(f'Ceйчас в Москве: {curtemp} градусов по цельсию')
