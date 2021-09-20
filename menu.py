# EXTERNAL MODULES
import os
from dotenv import load_dotenv
import json

# LOCAL MODULES
from api_requests import send_request, convert_json_file, convert_to_celcius, parse_weather_data
from diagram import create_humidity_chart, create_temperature_chart

load_dotenv()
API_KEY = os.getenv('API_KEY')

make_choice = True

while(make_choice):
    city = input("\n-GET FORECAST FOR A CITY-\n\nCity: ")
    choice = input("A. Temperature Chart\nB. Humidity Chart\nChoose type: ").capitalize()

    # if choice == "A" or "B":

    response = send_request(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}")

    if type(response) is bytes:

        weather_data = parse_weather_data(response)
        
        if choice == "A":
            create_temperature_chart(weather_data)
        elif choice == "B":
            create_humidity_chart(weather_data)
        else:
            print("Write either A or B to choose chart type")

    else:
        print("Error while parsing json_file")
        make_choice = True