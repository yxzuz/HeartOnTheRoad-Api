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
            '/api/traffic/{isTrafficJam}'.format(isTrafficJam=True),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
