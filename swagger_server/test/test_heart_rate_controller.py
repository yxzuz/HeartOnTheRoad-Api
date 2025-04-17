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

        # print(response_json)

    def test_get_heart_rate_trip_invalid(self):
        """Test case for invalid trip_id=999"""
        response = self.client.open(
            '/heart/v1/api/heartrate/trip/{trip_id}'.format(trip_id=999),
            method='GET')

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, [])

        # print(response.data.decode('utf-8'))

    def test_controller_get_heartrate_by_traffic(self):
        """Test case for controller_get_heartrate_by_traffic

        Get timestamped heart rate data filtered by traffic condition
        """
        # response = self.client.open(
        #     '/heart/v1/api/heartrate/traffic/{isTrafficJam}'.format(
        #         isTrafficJam=True),
        #     method='GET')
        response = self.client.open(
            '/heart/v1/api/heartrate/traffic/{omg}'.format(
                omg=True),
            method='GET')

        
        # response = self.client.open(
        #     #heart/v1/api/heartrate/traffic/true
        #     'http://127.0.0.1:8080/heart/v1/api/heartrate/traffic/true',
        #     method='GET')


        print(response.data.decode('utf-8'))
        # self.assert200(response,
        #                'Response body is : ' + response.data.decode('utf-8'))
        # # Parse the JSON response
        # response_json = json.loads(response.data.decode('utf-8'))

        # # Assert that the response is a non-empty object (trip summary)
        # self.assertIsInstance(response_json, list)


if __name__ == '__main__':
    import unittest
    unittest.main()
