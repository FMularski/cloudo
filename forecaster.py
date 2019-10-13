import requests


class Forecaster:
    def __init__(self):
        pass

    def get_weather(self, city):
        api_key = '19a79a6ddbd5fa9bf5ac7dc15cbdff49'
        url = 'http://api.openweathermap.org/data/2.5/forecast'  # ?q=Elblag
        params = {'APPID': api_key, 'q': city, 'units': 'Metric'}
        response = requests.get(url, params=params)

        self.format_response(response)

    def format_response(self, response):
        weather_info = []
