import matplotlib.pyplot as plt
import datetime

def convert_dates(dates):
    new_dates = []
    
    for date in dates:
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M%f')
        new_date = date.strftime("%d %b %H:%M")
        new_dates.append(new_date)
    return tuple(new_dates)

def zip_weather_data(weather_data):
    time, weather = zip(*weather_data.items())
    date = convert_dates(time)
    return date, weather

def create_temperature_chart(weather_data):

    date, weather = zip_weather_data(weather_data)
    temperature = []
    city_name = []
    city_country_code = []
    
    for i in weather:
        temperature.append(i[0])
        city_name.append(i[2])
        city_country_code.append(i[3])

    city = city_name[0]
    country_code = city_country_code[0]

    plt.figure(figsize=(35, 30), facecolor="floralwhite")
    plt.axes().set_facecolor('white')
    plt.title(f"Temperature forecast for {city}, {country_code}", fontdict={"fontsize" : "60"}, loc="center")
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
    plt.savefig(f"temperature_charts/temperature_forecast_{city}_{now}.png")
    print("Temperature forecast file created")
    plt.show()

def create_humidity_chart(weather_data):

    date, weather = zip_weather_data(weather_data)
    humidity = []
    city_country_code = []
    city_name = []

    for i in weather:
        humidity.append(i[1])
        city_name.append(i[2])
        city_country_code.append(i[3])

    city = city_name[0]
    country_code = city_country_code[0]

    plt.figure(figsize=(35, 30), facecolor="floralwhite")
    plt.axes().set_facecolor('white')
    plt.title(f"Humidity forecast for {city.capitalize()}, {country_code}", fontdict={"fontsize" : "60"}, loc="center")
    plt.ylabel(f"%", {"size": "40"}, loc="top", rotation="horizontal")
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=40)

    humidity_data = dict(zip(date, humidity))

    for x,y in humidity_data.items():
        plt.annotate(y, (x, y), ha="left", size="30")

    plt.plot(date, humidity, color="olivedrab", linewidth=5, marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
            markersize=12)

    plt.xticks(date, rotation="vertical")

    now = datetime.datetime.now()
    plt.savefig(f"humidity_charts/humidity_forecast_{city}_{now}.png")
    print("Humidity forecast file created")
    plt.show()