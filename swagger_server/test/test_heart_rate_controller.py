# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.heart_rate_trip import HeartRateTrip  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHeartRateController(BaseTestCase):
    """HeartRateController integration test stubs"""

    def test_get_heart_rate_trip_valid(self):
        """Test case for valid trip_id=1"""
        response = self.client.open(
            '/heart/v1/api/heartrate/trip/{trip_id}'.format(trip_id=1),
            method='GET')
        self.assert200(response, 'Response body is : ' +
                       response.data.decode('utf-8'))

        # Parse the JSON response
        response_json = json.loads(response.data.decode('utf-8'))

        # Assert that the response is a non-empty object (trip summary)
        self.assertIsInstance(response_json, list)
        self.assertGreater(len(response_json), 0,
                           'Response is empty, expected trip summary.')
        my_json_list = [
            {
                "heartrate": 74,
                "time": "2025-04-01T08:29:04Z"
            },
            {
                "heartrate": 76,
                "time": "2025-04-01T08:29:56Z"
            },
            {
                "heartrate": 71,
                "time": "2025-04-01T08:30:11Z"
            },
            {
                "heartrate": 74,
                "time": "2025-04-01T08:32:32Z"
            },
            {
                "heartrate": 72,
                "time": "2025-04-01T08:33:43Z"
            },
            {
                "heartrate": 77,
                "time": "2025-04-01T08:36:35Z"
            }
        ]
        self.assertEqual(response_json, my_json_list,
                         'Response does not match expected trip summary.')
        
    def test_get_heart_rate_trip_invalid(self):
        """Test case for invalid trip_id=29"""
        response = self.client.open(
            '/heart/v1/api/heartrate/trip/{trip_id}'.format(trip_id=29),
            method='GET')
        self.assert400(response,'Expected 400 Bad Request for negative trip_id')
        
    def test_get_heart_rate_trip_with_string_id(self):
        """Invalid string trip_id should return 500 (or 400 if you validate)"""
        response = self.client.open('/heart/v1/api/heartrate/trip/a', method='GET')
        self.assert500(response, 'Expected 500 Internal Server Error for invalid trip_id')

    def _get_heart_rate_trip_with_negative_id(self):
        """Negative trip_id should return 400"""
        response = self.client.open('/heart/v1/api/heartrate/trip/-2', method='GET')
        self.assert400(response, 'Expected 400 Bad Request for negative trip_id')


    def test_controller_get_heartrate_by_traffic(self):
        """Test case for controller_get_heartrate_by_traffic

        Get timestamped heart rate data filtered by traffic condition
        """
        response = self.client.open(
            '/heart/v1/api/heartrate/traffic/{is_traffic_jam}'.format(
                is_traffic_jam=True),
            method='GET')

        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        # Parse the JSON response
        response_json = json.loads(response.data.decode('utf-8'))

        # Assert that the response is a non-empty object (trip summary)
        self.assertIsInstance(response_json, list)


if __name__ == '__main__':
    import unittest
    unittest.main()
