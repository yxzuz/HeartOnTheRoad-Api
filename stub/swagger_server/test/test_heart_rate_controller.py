# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.heart_rate_trip import InlineResponse2003  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHeartRateController(BaseTestCase):
    """HeartRateController integration test stubs"""

    def test_get_heart_rate_trip(self):
        """Test case for get_heart_rate_trip

        Get heart rate data for a trip
        """
        response = self.client.open(
            '/api/heartrate/trip/{trip_id}'.format(trip_id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
