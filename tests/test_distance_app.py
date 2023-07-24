import unittest
from distance_app import app


class TestDistanceApp(unittest.TestCase):

    def setUp(self) -> None:

        self.app = app.test_client()
        self.app.testing = True
        self.city_1 = 'Москва'
        self.city_2 = 'Лондон'
        self.city_3 = 'Сидней'
        self.city_4 = '......'

    def test_cities_valid(self):

        """Проверка работы при вводе валидных данных"""

        response = self.app.post('/', data=dict(city_1=self.city_1, city_2=self.city_2))
        self.assertEqual(response.status_code, 200)

        self.assertIn(self.city_1, response.get_data(as_text=True))
        self.assertIn(self.city_2, response.get_data(as_text=True))
        self.assertIn("Расстояние:", response.get_data(as_text=True))

    def test_same_cities(self):

        """Проверка работы при вводе одного города в оба поля"""

        response = self.app.post('/', data=dict(city_1=self.city_1, city_2=self.city_1))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Вы ввели один и тот же город в оба поля.", response.get_data(as_text=True))

    def test_cities_invalid(self):

        """Проверка работы при вводе не валидных данных"""

        response = self.app.post('/', data=dict(city_1=self.city_1, city_2=self.city_4))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Возникла ошибка, проверьте правильность ввода.", response.get_data(as_text=True))
