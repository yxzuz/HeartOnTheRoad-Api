# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.trip_details import TripDetails  # InlineResponse2002  # noqa: E501
from swagger_server.models.number_of_trip import NumberOfTrip  # InlineResponse2005  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTripController(BaseTestCase):
    """TripController integration test stubs"""

    def test_get_number_of_trips(self):
        """Test case for get_number_of_trips

        Get number of trips
        """
        response = self.client.open(
            '/heart/v1/api/trip',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(response_data['number_of_trip'], (int, float))

    def test_get_trip_details(self):
        """Test case for get_trip_details

        Get trip details
        """
        response = self.client.open(
            '/heart/v1/api/trip/{trip_id}'.format(trip_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(response_data, dict)
        self.assertIn('average_heartrate', response_data)
        self.assertIn('duration', response_data)
        self.assertIn('max_heartrate', response_data)
        self.assertIn('min_heartrate', response_data)
        self.assertIn('record', response_data)
        self.assertIn('start_time', response_data)
    
    def test_get_trip_details_invalid(self):
        """Test case for invalid trip_id=999"""
        response = self.client.open(
            '/heart/v1/api/trip/{trip_id}'.format(trip_id=999),
            method='GET')
        self.assert400(response,'Expected 400 Bad Request for negative trip_id')
        
    def test_get_trip_details_with_string_id(self):
        """Invalid string trip_id should return 500 (or 400 if you validate)"""
        response = self.client.open('/heart/v1/api/trip/a', method='GET')
        self.assert500(response, 'Expected 500 Internal Server Error for invalid trip_id')

    def test_get_trip_details_with_negative_id(self):
        """Negative trip_id should return 400"""
        response = self.client.open('/heart/v1/api/trip/-2', method='GET')
        self.assert400(response, 'Expected 400 Bad Request for negative trip_id')


if __name__ == '__main__':
    import unittest
    unittest.main()
