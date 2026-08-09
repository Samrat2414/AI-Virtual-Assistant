import json
import urllib.parse
import urllib.request


class WeatherManager:

    def get_weather(self, city):

        try:
            # Find city coordinates
            city_url = (
                "https://geocoding-api.open-meteo.com/v1/search?"
                + urllib.parse.urlencode({
                    "name": city,
                    "count": 1,
                    "language": "en",
                    "format": "json"
                })
            )

            with urllib.request.urlopen(
                city_url,
                timeout=10
            ) as response:

                location_data = json.loads(
                    response.read().decode("utf-8")
                )

            if "results" not in location_data:
                return f"I couldn't find the city {city}."

            location = location_data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]
            city_name = location["name"]

            # Get current weather
            weather_url = (
                "https://api.open-meteo.com/v1/forecast?"
                + urllib.parse.urlencode({
                    "latitude": latitude,
                    "longitude": longitude,
                    "current": (
                        "temperature_2m,"
                        "relative_humidity_2m,"
                        "apparent_temperature,"
                        "weather_code,"
                        "wind_speed_10m"
                    ),
                    "timezone": "auto"
                })
            )

            with urllib.request.urlopen(
                weather_url,
                timeout=10
            ) as response:

                weather_data = json.loads(
                    response.read().decode("utf-8")
                )

            current = weather_data["current"]

            temperature = current["temperature_2m"]
            feels_like = current["apparent_temperature"]
            humidity = current["relative_humidity_2m"]
            wind = current["wind_speed_10m"]

            return (
                f"Weather in {city_name}: "
                f"{temperature}°C, "
                f"feels like {feels_like}°C, "
                f"humidity {humidity}%, "
                f"wind {wind} km/h."
            )

        except Exception:
            return (
                "Sorry, I couldn't get the weather right now."
            )