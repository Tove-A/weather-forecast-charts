import requests
# import os
# from dotenv import load_dotenv
import json

# load_dotenv()
# API_KEY = os.getenv('API_KEY')

def send_request(request):

    try:
        response = requests.get(request)
        if response.status_code == 200:
            print('Request successful!')
            return response.content

        if response.status_code == 404:
            print("City not found")
            return None

        else:
            print(f'Request errorcode: {response.status_code}')
            return None

    except requests.exceptions.RequestException as e:
        print(f'{e}')


def convert_json_file(json_file):
    
    if type(json_file) is bytes:
        data = json.loads(json_file)
        return data
    else:
        print("Error while converting json file into dictionary")
        return None

def convert_to_celcius(kelvin_degrees):
    celsius = kelvin_degrees - 273.15
    return celsius

def parse_weather_data(response):

    weather_info = convert_json_file(response)
    city_info = weather_info["city"]
    city_name = city_info["name"]
    city_country_code = city_info["country"]

    weather_data = {}

    for info in weather_info["list"]:
        temp = info["main"]["temp"]
        humidity = info["main"]["humidity"]
        time = info["dt_txt"]
        time = time[:-3]

        info = [] 
        info.append(round(convert_to_celcius(temp), 2))
        info.append(humidity)
        info.append(city_name)
        info.append(city_country_code)

        weather_data[time] = info
    return weather_data