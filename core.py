import requests
import json
from config import WEATHER, TELEGRAM

class Weather:
    def __init__(self):
        self.url = WEATHER['url']
        self.city = WEATHER['city']
        self.country_code = WEATHER['country_code']
        self.appid = WEATHER['appid']

    def get_weather_in_the_city(self):
        get_weather = requests.get(self.url+"?q="+self.city+","+self.country_code+"&appid="+self.appid)
        get_weather = json.loads(get_weather.text)
        if get_weather['cod'] == 200:
            return "Weather in "+get_weather['name']+\
                   ":\n - temperature: "+str(get_weather['main']['temp'] - 273.15)+"℃"+\
                   ";\n - pressure: "+str(get_weather['main']['pressure'])+\
                   ";\n- humidity: "+str(get_weather['main']['humidity'])+"% ."

class Telegram:
    def __init__(self):
        self.url = TELEGRAM['url']
        self.chanel = TELEGRAM['chanel']
        self.token = TELEGRAM['token']

    def send_mesasge(self, message):
        send_message = requests.post(
            self.url+self.token+"/sendMessage",
            data={
                "chat_id": self.chanel,
                "text": message
            }
        )
        if send_message.status_code != 200:
            raise Exception("Message failed to send!")
