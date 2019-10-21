from core import Weather, Telegram

send = Telegram()
mes = Weather()

if __name__ == '__main__':
  send.send_mesasge(mes.get_weather_in_the_city())
