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
            '/api/location/trip/{trip_id}'.format(trip_id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        
    def test_controller_get_speed_by_traffic(self):
        """Test case for controller_get_speed_by_traffic

        Get current speed data filtered by traffic condition
        """
        response = self.client.open(
            '/api/speed/traffic/{isTrafficJam}'.format(is_traffic_jam=true),
            method='GET')
        self.assert200(response,
                        'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
