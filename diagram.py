import matplotlib.pyplot as plt
import numpy as np
import datetime
from api_requests import weather_data, city_country_code, city_name, choice

time, weather = zip(*weather_data.items())

temperature = []
humidity = []
weather_description = []

for i in weather:
    temperature.append(i[0])
    humidity.append(i[1])
    weather_description.append(i[2])

def convert_dates(dates):
    new_dates = []
    
    for date in dates:
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M%f')
        new_date = date.strftime("%d %b %H:%M")
        new_dates.append(new_date)
    return tuple(new_dates)

date = convert_dates(time)

def create_temperature_chart():

    plt.figure(figsize=(35, 30), facecolor="floralwhite")
    plt.axes().set_facecolor('white')
    plt.title(f"Temperature forecast for {city_name.capitalize()}, {city_country_code}", fontdict={"fontsize" : "60"}, loc="center")
    plt.ylabel(f"°C", {"size": "40"}, loc="top", rotation="horizontal")
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=40)

    temperature_data = dict(zip(date, temperature))

    for x,y in temperature_data.items():
        plt.annotate(y, (x, y), ha="left", size="30")


    plt.plot(date, temperature, color="olivedrab", linewidth=5, marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
            markersize=12)
    plt.xticks(date, rotation="vertical")

    now = datetime.datetime.now()
    plt.savefig(f"temperature_forecast_{city_name}_{now}.png")
    print("Temperature forecast file created")
    plt.show()

def create_humidity_chart():
    
    plt.figure(figsize=(35, 30), facecolor="floralwhite")
    plt.axes().set_facecolor('white')
    plt.title(f"Humidity forecast for {city_name.capitalize()}, {city_country_code}", fontdict={"fontsize" : "60"}, loc="center")
    plt.ylabel(f"%", {"size": "40"}, loc="top", rotation="horizontal")
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=40)

    humidity_data = dict(zip(date, humidity))

    for x,y in humidity_data.items():
        plt.annotate(y, (x, y), ha="left", size="20")

    plt.plot(date, humidity, color="olivedrab", linewidth=5, marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
            markersize=12)

    plt.xticks(date, rotation="vertical")

    now = datetime.datetime.now()
    plt.savefig(f"humidity_forecast_{city_name}_{now}.png")
    print("Humidity forecast file created")
    plt.show()

def create_chart():
    if choice == "A":
        create_temperature_chart()
    elif choice == "B":
        create_humidity_chart()
    else:
        print("Write either A or B to choose chart type")