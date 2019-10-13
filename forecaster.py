import requests


class Forecaster:
    def __init__(self):
        pass

    def get_weather(self, city):
        api_key = '19a79a6ddbd5fa9bf5ac7dc15cbdff49'
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        params = {'APPID': api_key, 'q': city, 'units': 'Metric'}
        response = requests.get(url, params=params)

        self.format_response(response.json())

    def format_response(self, response):
        record = ''
        for i in range(0, response['cnt']):
            record += f"--== {response['city']['name']}, {response['city']['country']} "
            record += f"{response['list'][i]['dt_txt']} ==--\n" + f"Description: "
            record += f"{response['list'][i]['weather'][0]['description']}\n"
            record += f"Temperature: {response['list'][i]['main']['temp']}°C\tmax: "
            record += f"{response['list'][i]['main']['temp_max']}°C"
            record += f"\tmin: {response['list'][i]['main']['temp_min']}°C\n"
            record += f"Pressure: {response['list'][i]['main']['pressure']} hPa\n"
            record += f"Humidity: {response['list'][i]['main']['humidity']}%\n"
            record += f"Clouds: {response['list'][i]['clouds']['all']}%\n"
            record += f"Wind: {response['list'][i]['wind']['speed']} km/h\n\n"
        return record
