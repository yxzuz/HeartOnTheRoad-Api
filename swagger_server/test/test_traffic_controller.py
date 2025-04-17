# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.traffic_summary import TrafficSummary  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrafficController(BaseTestCase):
    """TrafficController integration test stubs"""

    def test_controller_get_traffic_summary(self):
        """Test case for controller_get_traffic_summary

        Get summary statistics for heart rate and traffic by traffic condition
        """
        response = self.client.open(
            '/heart/v1/api/traffic/{is_traffic_jam}'.format(
                is_traffic_jam=True),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        response_data = json.loads(response.data.decode('utf-8'))
        # check structure
        self.assertIn('average_heartrate', response_data)
        self.assertIn('average_speed', response_data)
        self.assertIn('average_travel_time', response_data)
        self.assertIn('max_heartrate', response_data)
        self.assertIn('min_heartrate', response_data)
        self.assertIn('number_of_records', response_data)
        self.assertIsInstance(response_data, dict)


if __name__ == '__main__':
    import unittest
    unittest.main()
