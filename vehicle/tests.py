from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_car(self):
        """ тестирование создания машин """

        data = {
            'car_title': 'Test',
            'car_description': 'TestTest'
        }

        response = self.client.post(
            '/cars/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'milage': [], 'car_title': 'Test', 'car_description': 'TestTest', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

    def test_list_car(self):
        """ тестирование списка машин """

        Car.objects.create(
            car_title='Test_list',
            car_description='Test_list'
        )

        response = self.client.get(
            '/cars/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [{'id': 2, 'milage': [], 'car_title': 'Test_list', 'car_description': 'Test_list', 'owner': None}]
        )
