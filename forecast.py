# EXTERNAL MODULES
import os
from dotenv import load_dotenv
import json

# LOCAL MODULES
from api_requests import send_request, convert_json_file, convert_to_celcius, parse_weather_data
from diagram import create_humidity_chart, create_temperature_chart

# Load the api key from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

make_choice = True

# Menu with choices
while(make_choice):

    # Menu options
    city = input("\n-GET FORECAST FOR A CITY-\n\nCity: ")
    choice = input("A. Temperature Chart\nB. Humidity Chart\nQ. Quit program\nChoose type: ").capitalize()

    # Sending the request
    response = send_request(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}")

    # Make sure the response type is correct
    if type(response) is bytes:

        # Parsing the response
        weather_data = parse_weather_data(response)
        
        if choice == "A":
            # Creating a temperature chart with the data
            create_temperature_chart(weather_data)

        elif choice == "B":
            # Creating a humidity chart with the data
            create_humidity_chart(weather_data)

        elif choice == "Q":
            exit("Program exits")

        else:
            print("Write either A or B to choose chart type")

    else:
        print("Error while parsing json_file")
        make_choice = True