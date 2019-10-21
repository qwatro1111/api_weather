import unittest
from config import WEATHER, TELEGRAM
from core import Weather, Telegram

class MyTestConfig(unittest.TestCase):
    """ Test config.py """
    def test_config_weather_url(self):
        self.assertTrue(bool(WEATHER['url']))
    def test_config_weather_city(self):
        self.assertTrue(bool(WEATHER['city']))
    def test_config_weather_country_code(self):
        self.assertTrue(bool(WEATHER['country_code']))
    def test_config_weather_appid(self):
        self.assertTrue(bool(WEATHER['appid']))

    def test_config_telegram_url(self):
        self.assertTrue(bool(TELEGRAM['url']))
    def test_config_telegram_chanel(self):
        self.assertTrue(bool(TELEGRAM['chanel']))
    def test_config_telegram_token(self):
        self.assertTrue(bool(TELEGRAM['token']))

class MyTestCere(unittest.TestCase):
    """ Test core.py """
    def test_core_wether(self):
        check = Weather()
        self.assertTrue(bool(check.get_weather_in_the_city()))


if __name__ == '__main__':
    unittest.main()
