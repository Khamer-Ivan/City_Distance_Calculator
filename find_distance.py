from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from typing import Tuple, Any
import requests
import os


def get_coordinates(city_name: str) -> Tuple[float, float]:

    """
   Method for getting the coordinates of the city

    :param city_name: str
    :return: Tuple[float, float]
    """

    geolocator = Nominatim(user_agent="city_distance_calculator")
    location = geolocator.geocode(city_name)
    if location is None:
        raise ValueError("City not found")

    return location.latitude, location.longitude


def calculate_distance(city1: str, city2: str) -> float:

    """
   A method for calculating the distance between two cities

    :param city1: str
    :param city2: str
    :return: float
    """

    try:
        latitude1, longitude1 = get_coordinates(city1)
        latitude2, longitude2 = get_coordinates(city2)

        distance: float = geodesic((latitude1, longitude1), (latitude2, longitude2)).kilometers

        return distance

    except ValueError as e:

        return str(e)


def get_road_distance(city1: str, city2: str) -> Any:

    """
    A method for calculating the distance between two cities by road

    :param city1: str
    :param city2: str
    :return: Any
    """

    try:
        location1: tuple = get_coordinates(city1)
        location2: tuple = get_coordinates(city2)

        url = "https://api.openrouteservice.org/v2/directions/driving-car"

        api_key = os.getenv('API_KEY')
        params = {
            "api_key": api_key,
            "start": f"{location1[1]},{location1[0]}",
            "end": f"{location2[1]},{location2[0]}",
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "features" in data and data["features"]:
            road_distance = data["features"][0]["properties"]["segments"][0]["distance"]
            return road_distance / 1000
        else:
            return 'It is impossible to plot a car route.'

    except ValueError as e:
        return str(e)
