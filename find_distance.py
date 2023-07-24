from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from typing import Tuple, Any
import requests


def get_coordinates(city_name: str) -> Tuple[float, float]:

    """
    Метод для получения координат города

    :param city_name: str
    :return: Tuple[float, float]
    """

    geolocator = Nominatim(user_agent="city_distance_calculator")
    location = geolocator.geocode(city_name)
    if location is None:
        raise ValueError("Город не найден")

    return location.latitude, location.longitude


def calculate_distance(city1: str, city2: str) -> float:

    """
    Метод для вычисления расстояния между двумя городами

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
    Метод для вычисления расстояния между двумя городами по дорогам

    :param city1: str
    :param city2: str
    :return: Any
    """

    try:
        location1: tuple = get_coordinates(city1)
        location2: tuple = get_coordinates(city2)

        url = "https://api.openrouteservice.org/v2/directions/driving-car"
        params = {
            "api_key": "5b3ce3597851110001cf624891e2eb0ae04b4436bfd9587220f7f28d",
            "start": f"{location1[1]},{location1[0]}",
            "end": f"{location2[1]},{location2[0]}",
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "features" in data and data["features"]:
            road_distance = data["features"][0]["properties"]["segments"][0]["distance"]
            return road_distance / 1000  # Переводим в километры
        else:
            return 'Невозможно проложить автомобильный маршрут.'

    except ValueError as e:
        return str(e)
