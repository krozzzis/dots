#!/bin/env python3

import requests


def get_location(city: str) -> (float, float):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': city,
        'format': 'jsonv2',
        'limit': 1  # Ограничиваем до одного результата
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return (latitude, longitude)
        else:
            return None
    else:
        return None


def weather_icon(weather_code: int):
    weather_icons = {
        0: "☀️",
        1: "🌤",
        2: "⛅",
        3: "☁️",
        45: "🌫",
        48: "🌫",
        51: "🌦",
        61: "🌧",
        80: "⛈",
        85: "❄️",
        95: "🌪",
    }

    return weather_icons.get(weather_code, "❓")


def get_current(latitude: float, longitude: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['current_weather']
    else:
        return None



def main():
    latitude, longitude = 56.839104, 60.60825
    weather_data = get_current(latitude, longitude)

    temperature = weather_data['temperature']
    weather_code = weather_data['weathercode']
    
    icon = weather_icon(weather_code)

    print(f"{icon} {temperature}°C")


if __name__ == "__main__":
    main()
