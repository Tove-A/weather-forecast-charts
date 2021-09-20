  

<br  />

<p  align="center">

<h1  align="center">Weather forecast charts</h1>

  

<p  align="center">

This is a program that generates temperature and humidity forecast charts for any city. Using <a  href="https://openweathermap.org/api">Open Weather Map API</a>

<details  open="open">

<summary><h2  style="display: inline-block">Table of Contents</h2></summary>



<li><a  href="#built-with">Built With</a></li>
</ul>

</li>

<li>
<a  href="#getting-started">Getting Started</a>

<li><a  href="#prerequisites">Prerequisites</a></li>

<li><a  href="#installation">Installation</a></li>

<li><a  href="#usage">Usage</a></li>

</ul>

</li>

<li><a  href="#contact">Contact</a></li>

</ol>

</details>


### Built With

*  [Python](https://www.python.org/)

## Getting Started

  

### Prerequisites

  

* Download the latest version of [Python](https://www.python.org/)

* Create a free account at Open Weather Map and create an [API KEY](https://home.openweathermap.org/api_keys)

  

### Installation

1. Clone the repository

```sh

git clone https://github.com/Tove-A/forecast-charts

```

2. Navigate into your cloned folder


```sh

cd  "Drive:/folder/folder/forecast-charts"

```

3. Install the following modules:

  

```sh

pip install requests

pip install matplotlib

pip install dotenv

```

  

<!-- USAGE EXAMPLES -->

## Usage

  

1. Rename the .env.example file to .env

2. In the .env file, replace the text with your api key </br>

  

```sh

API_KEY = "YOUR API KEY"

```

3. Run the program

  

```sh

python forecast.py

```

<!-- COMMANDS -->

## Running the program

  Choose a city

```sh

-GET FORECAST FOR A CITY-

City:

```
Choose chart, type A for a temperature chart or B for a humidity chart
```sh

A. Temperature Chart
B. Humidity Chart
Choose type:

```
A .png file with the chart will be available in a folder within the forecast directory

#### Humidity charts

  ```sh

cd humidity_charts
code temperature_forecast_city_2021...

```
#### Temperature charts
  ```sh

cd humidity_charts
code humidity_forecast_city_2021...

```




## Contact

  

[Tove Andersson](https://github.com/Tove-A) - toveandersson13@gmail.com | [LinkedIn](https://www.linkedin.com/in/tove-andersson-75ab83165/)

