import requests
import time
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

from agentlite.actions import BaseAction

URLS = {
    "historical_weather": "https://archive-api.open-meteo.com/v1/archive",
    "geocoding": "https://geocoding-api.open-meteo.com/v1/search",
    "air_quality": "https://air-quality-api.open-meteo.com/v1/air-quality",
    "elevation": "https://api.open-meteo.com/v1/elevation",
    "zipcode": "http://ZiptasticAPI.com/{zipcode}",
    "weather_forecast": "https://api.open-meteo.com/v1/forecast",
}

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

class get_user_current_date(BaseAction):
    def __init__(self) -> None:
        action_name = "get_user_current_date"
        action_desc = "get the current date of the user"
        params_doc = {
            "None": "No input required"
        }
        super().__init__(action_name, action_desc, params_doc)
        
    def __call__(self, **kwargs):
        return time.strftime("%Y-%m-%d %H:%M:%S")

class get_user_current_location(BaseAction):
    def __init__(self) -> None:
        action_name = "get_user_current_location"
        action_desc = "get the current location of the user"
        params_doc = {
            "None": "No input required"
        }
        super().__init__(action_name, action_desc, params_doc)
        
    def __call__(self, **kwargs):
        location = "Palo Alto"
        return location
    
class get_latitude_longitude(BaseAction):
    def __init__(self) -> None:
        action_name = "get_latitude_longitude"
        action_desc = "Get latitude and longitude information for a specified location name."
        params_doc = {
            "name": "(Type: string): The name of the location. (e.g., city name)"
        }
        super().__init__(action_name, action_desc, params_doc)
    
    def _clean(self, response):
        for item in response["results"]:
            if "elevation" in item.keys():
                item.pop("elevation")
            if "feature_code" in item.keys():
                item.pop("feature_code")
            if "country_code" in item.keys():
                item.pop("country")
            if "country_id" in item.keys():
                item.pop("country_id")
            if "admin1_id" in item.keys():
                item.pop("admin1_id")
            if "timezone" in item.keys():
                item.pop("timezone")
            if "population" in item.keys():
                item.pop("population")
            if "postcodes" in item.keys():
                item.pop("postcodes")
            for key in list(item.keys()):
                if key.endswith("id"):
                    item.pop(key)
            for key in list(item.keys()):
                if "admin" in key:
                    item.pop(key)
        if "generationtime_ms" in response.keys():
            response.pop("generationtime_ms")
        return response
        
    def __call__(self, **kwargs):
        params = {
            "name": kwargs["name"],
            "count": 3,
            "language": "en",
            "format": "json"
        }
        response = requests.get(URLS["geocoding"], params=params)
        if response.status_code == 200:
            return str(self._clean( response.json()))
        else:
            return response.text

class get_weather_forcast(BaseAction):
    def __init__(self, env = None) -> None:
        action_name = "get_weather_forcast"
        action_desc = "Get weather forcast for a specified location. Return the current temperature in °F and rain probability."
        params_doc = {
            "latitude": "The latitude of the location",
	        "longitude": "The longitude of the location",
        }
        self.url = "https://api.open-meteo.com/v1/forecast"
        super().__init__(action_name, action_desc, params_doc)
        
    def __call__(self, **kwargs):
        params = {
            "latitude": kwargs["latitude"],
            "longitude": kwargs["longitude"],
            "current": ["temperature_2m", "rain"],
            "hourly": "temperature_2m",
            "temperature_unit": "fahrenheit"
        }
        responses = openmeteo.weather_api(self.url, params=params)
        observation = ""
        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        # observation += f"Coordinates {response.Latitude()}°N {response.Longitude()}°E"
        # observation += f"Elevation {response.Elevation()} m asl"
        # # Current values. The order of variables needs to be the same as requested.
        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()
        current_rain = current.Variables(1).Value()

        # observation += f"Current time {current.Time()}"
        observation += f"Current temperature {current_temperature_2m} F\n"
        observation += f"Current rain {current_rain}"
        return observation

if __name__ == "__main__":
    action = get_user_current_date()
    print(action())
    action = get_user_current_location()
    print(action())
    action = get_latitude_longitude()
    print(type(action(name="Palo Alto")))
    action = get_weather_forcast()
    print(action(latitude=20.54065, longitude=-100.2213))