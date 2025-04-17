# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.location_trip import LocationTrip  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLocationController(BaseTestCase):
    """LocationController integration test stubs"""

    def test_get_location_trip(self):
        """Test case for get_location_trip

        Get location data for a trip
        """
        response = self.client.open(
            '/heart/v1/api/location/trip/{trip_id}'.format(trip_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        
        response2 = self.client.open(
            '/heart/v1/api/location/trip/{trip_id}'.format(trip_id='1'),
            method='GET')
        self.assert200(response2,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_location_trip_invalid(self):
        """Test case for invalid trip_id=29"""
        response = self.client.open(
            '/heart/v1/api/location/trip/{trip_id}'.format(trip_id=29),
            method='GET')
        self.assert400(response,'Expected 400 Bad Request for negative trip_id')
        
    def test_get_location_trip_with_string_id(self):
        """Invalid string trip_id should return 500 (or 400 if you validate)"""
        response = self.client.open('/heart/v1/api/location/trip/a', method='GET')
        self.assert500(response, 'Expected 500 Internal Server Error for invalid trip_id')

    def test_get_location_trip_with_negative_id(self):
        """Negative trip_id should return 400"""
        response = self.client.open('/heart/v1/api/location/trip/-2', method='GET')
        self.assert400(response, 'Expected 400 Bad Request for negative trip_id')

    def test_controller_get_speed_by_traffic(self):
        """Test case for controller_get_speed_by_traffic

        Get current speed data filtered by traffic condition
        """
        response = self.client.open(
            '/heart/v1/api/speed/traffic/{is_traffic_jam}'.format(
                is_traffic_jam=True),
            method='GET')
        response_json = json.loads(response.data.decode('utf-8'))   
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertIsInstance(response_json, list)


if __name__ == '__main__':
    import unittest
    unittest.main()
