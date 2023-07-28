import unittest
from distance_app import app


class TestDistanceApp(unittest.TestCase):

    def setUp(self) -> None:

        self.app = app.test_client()
        self.app.testing = True
        self.city_1 = 'Moscow'
        self.city_2 = 'London'
        self.city_3 = 'Sidney'
        self.city_4 = '......'

    def test_cities_valid(self):

        """Checking the operation when entering valid data"""

        response = self.app.post('/', data=dict(city_1=self.city_1, city_2=self.city_2))
        self.assertEqual(response.status_code, 200)

        self.assertIn(self.city_1, response.get_data(as_text=True))
        self.assertIn(self.city_2, response.get_data(as_text=True))
        self.assertIn("Distance:", response.get_data(as_text=True))

    def test_same_cities(self):

        """Checking the operation when entering one city in both fields"""

        response = self.app.post('/', data=dict(city_1=self.city_1, city_2=self.city_1))
        self.assertEqual(response.status_code, 200)
        self.assertIn("You entered the same city in both fields.", response.get_data(as_text=True))

    def test_cities_invalid(self):

        """Checking the operation when entering invalid data"""

        response = self.app.post('/', data=dict(city_1=self.city_1, city_2=self.city_4))
        self.assertEqual(response.status_code, 200)
        self.assertIn("An error has occurred, check the correctness of the input.", response.get_data(as_text=True))
