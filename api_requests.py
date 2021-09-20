import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv('API_KEY')

weather_data = ""
city_info = ""
city_id = ""
city_name = ""
city_country_code = ""

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

make_choice = True

while(make_choice):
    city = input("-GET FORECAST FOR A CITY-\n\nCity: ")
    choice = input("A. Temperature Chart\nB. Humidity Chart\nChoose type: ").capitalize()

    if choice == "A" or "B":

        response = send_request(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}")

        if type(response) is bytes:

            make_choice = False

            weather_info = convert_json_file(response)
            city_info = weather_info["city"]
            city_id = city_info["id"]
            city_name = city_info["name"]
            city_country_code = city_info["country"]

            weather_data = {}

            for info in weather_info["list"]:
                temp = info["main"]["temp"]
                humidity = info["main"]["humidity"]
                time = info["dt_txt"]
                time = time[:-3]
                weather_description = info["weather"][0]["description"]

                info = [] 
                info.append(round(convert_to_celcius(temp), 2))
                info.append(humidity)
                info.append(weather_description)

                weather_data[time] = info

        else:
            print("Error while parsing json_file")
            make_choice = True