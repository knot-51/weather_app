# Weather App
A simple Python weather app that retrieves and displays current weather information for a city using the OpenWeatherMap API. Built with `requests` and supports `.env` configuration to keep the API key secure.

## Features
- Get current temperature
- Feels-like temperature
- Weather description
- Humidity and wind speed
- Securely manage API key with environment variables
- Simple CLI (command-line) interface

---

## Requirements
- Python 3.12+
- [OpenWeatherMap API key](https://openweathermap.org/api)

## Installation
1. **Clone the repository**
```bash
git clone https://github.com/knot-51/weather_app.git
cd weather_app
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Set up your environment variables**
- Create a .env file
```bash
touch .env
```
- Add your API key from OpenWeatherMap into .env file
```bash
API_KEY = your_api_key_here
```

## How to use
```bash
python main.py
```
- Add city name into the box and click the "Get Weather" button
- Get the weather information
