import requests
import json


def getWeather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Bangalore,in&units=metric&appid=7496fe2f717810e072f9a08ed5405e70'
    res = requests.get(url)
    weatherStr = res.text
    weatherDict=json.loads(weatherStr)
    return weatherDict['main']['temp']
