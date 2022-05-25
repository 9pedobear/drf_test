from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from car.models import *
from car.serializers import *
from pprint import pprint

class CarAPITestCase(APITestCase):
    def test_get(self):
        car1 = Car.objects.create(name='BMW', price=25000)
        car2 = Car.objects.create(name='Lexus', price=35000)
        car3 = Car.objects.create(name='Bugati', price=55000)
        print(car1.name, car2.name, car3.name)
        url = reverse('car-list')
        print(url)
        response = self.client.get(url)
        print(response)
        serializer_data = CarSerializer([car1, car2, car3], many=True).data
        for sd in serializer_data:
            print(sd)
        pprint([status.HTTP_200_OK, response.status_code, serializer_data, response.data])
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)














