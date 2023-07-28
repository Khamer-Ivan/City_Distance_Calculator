import unittest

from find_distance import get_coordinates, get_road_distance, calculate_distance


class TestFindDistance(unittest.TestCase):

    def setUp(self) -> None:

        self.city_1 = 'Moscow'
        self.city_2 = 'London'
        self.city_3 = 'Sidney'
        self.city_4 = '.......'

    def test_get_coordinates_valid(self):

        """Checking the receipt of coordinates when entering valid data"""

        answer = get_coordinates(self.city_1)
        self.assertEqual(round(answer[0], 4), 55.7504)
        self.assertEqual(round(answer[1], 4), 37.6175)

    def test_get_coordinates_invalid(self):

        """Checking for obtaining coordinates when entering invalid data"""

        with self.assertRaises(ValueError):
            get_coordinates(self.city_4)

    def test_calculate_distance_valid(self):

        """Checking the calculation of the distance in a straight line when entering valid data"""

        answer = calculate_distance(self.city_1, self.city_2)
        self.assertEqual(round(answer, 2), 2508.63)

    def test_calculate_distance_invalid(self):

        """Checking the calculation of the distance in a straight line when entering invalid data"""

        answer = calculate_distance(self.city_1, self.city_4)
        self.assertEqual(answer, "City not found")

    def test_get_road_distance_valid_1(self):

        """Checking the calculation of the distance along the roads when entering valid data"""

        answer = get_road_distance(self.city_1, self.city_2)
        self.assertEqual(round(answer, 2), 2896.35)

    def test_get_road_distance_valid_2(self):

        """Checking the calculation of the distance on the roads in the absence of a car route"""

        answer = get_road_distance(self.city_1, self.city_3)
        self.assertEqual(answer, "It is impossible to plot a car route.")

    def test_get_road_distance_invalid(self):

        """Checking the calculation of the distance on roads when entering invalid data"""

        answer = get_road_distance(self.city_1, self.city_4)
        self.assertEqual(answer, "City not found")
