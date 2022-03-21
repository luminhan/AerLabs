import decimal

from django.test import TestCase, Client
from django.urls import reverse
from http import HTTPStatus
from airport.models import Airport


class ApiMethodTest(TestCase):
    """Test if only GET method is allowed"""
    def setUp(self):
        self.url = reverse('aircraft-get', kwargs={'code': 'AMS'})
        self.client = Client()
        Airport(
            Id=2513,
            type='large_airport',
            name='Amsterdam Airport Schiphol',
            latitude_deg=decimal.Decimal(52.308601),
            longitude_deg=decimal.Decimal(4.76389),
            gps_code='EHAM',
            iata_code='AMS'
        ).save()

    def test_api_method_get(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_api_method_post(self):
        res = self.client.post(self.url)
        self.assertEqual(res.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_api_method_put(self):
        res = self.client.put(self.url)
        self.assertEqual(res.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_api_method_patch(self):
        res = self.client.patch(self.url)
        self.assertEqual(res.status_code, HTTPStatus.METHOD_NOT_ALLOWED)


class InvalidAirportCodeTest(TestCase):
    """Test if 404 returned with invalid airport code"""
    def setUp(self):
        self.url = reverse('aircraft-get', kwargs={'code': 'AERLABS'})
        self.client = Client()

    def test_invalid_airport_code(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, HTTPStatus.NOT_FOUND)


class ValidAirportCodeTest(TestCase):
    """Test if OK returned with valid airport code"""
    def setUp(self):
        self.url = reverse('aircraft-get', kwargs={'code': 'AMS'})
        self.client = Client()
        Airport(
            Id=2513,
            type='large_airport',
            name='Amsterdam Airport Schiphol',
            latitude_deg=decimal.Decimal(52.308601),
            longitude_deg=decimal.Decimal(4.76389),
            gps_code='EHAM',
            iata_code='AMS'
        ).save()

    def test_valid_airport_code(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertEqual(res['content-type'], 'application/json')
