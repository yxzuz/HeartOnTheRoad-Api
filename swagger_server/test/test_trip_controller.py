# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.trip_details import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTripController(BaseTestCase):
    """TripController integration test stubs"""

    def test_get_number_of_trips(self):
        """Test case for get_number_of_trips

        Get number of trips
        """
        response = self.client.open(
            '/api/trip',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_trip_details(self):
        """Test case for get_trip_details

        Get trip details
        """
        response = self.client.open(
            '/api/trip/{trip_id}'.format(trip_id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
