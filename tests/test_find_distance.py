import unittest

from find_distance import get_coordinates, get_road_distance, calculate_distance


class TestFindDistance(unittest.TestCase):

    def setUp(self) -> None:

        self.city_1 = 'Москва'
        self.city_2 = 'Лондон'
        self.city_3 = 'Сидней'
        self.city_4 = '.......'

    def test_get_coordinates_valid(self):

        """Проверка получения координат при вводе валидных данных"""

        answer = get_coordinates(self.city_1)
        self.assertEqual(round(answer[0], 4), 55.7504)
        self.assertEqual(round(answer[1], 4), 37.6175)

    def test_get_coordinates_invalid(self):

        """Проверка получения координат при вводе не валидных данных"""

        with self.assertRaises(ValueError):
            get_coordinates(self.city_4)

    def test_calculate_distance_valid(self):

        """Проверка вычисления расстояния по прямой при вводе валидных данных"""

        answer = calculate_distance(self.city_1, self.city_2)
        self.assertEqual(round(answer, 2), 2508.63)

    def test_calculate_distance_invalid(self):

        """Проверка вычисления расстояния по прямой при вводе не валидных данных"""

        answer = calculate_distance(self.city_1, self.city_4)
        self.assertEqual(answer, "Город не найден")

    def test_get_road_distance_valid_1(self):

        """Проверка вычисления расстояния по дорогам при вводе валидных данных"""

        answer = get_road_distance(self.city_1, self.city_2)
        self.assertEqual(round(answer, 2), 2896.35)

    def test_get_road_distance_valid_2(self):

        """Проверка вычисления расстояния по дорогам при отсутствии автомобильного маршрута"""

        answer = get_road_distance(self.city_1, self.city_3)
        self.assertEqual(answer, "Невозможно проложить автомобильный маршрут.")

    def test_get_road_distance_invalid(self):

        """Проверка вычисления расстояния по дорогам при вводе не валидных данных"""

        answer = get_road_distance(self.city_1, self.city_4)
        self.assertEqual(answer, "Город не найден")
