# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.analytic_relation import InlineResponse2001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnalyticsController(BaseTestCase):
    """AnalyticsController integration test stubs"""

    def test_get_analytic_data(self):
        """Test case for get_analytic_data

        Get analytics data
        """
        response = self.client.open(
            '/api/analytic',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_analytic_relation(self):
        """Test case for get_analytic_relation

        Get heart rate and traffic ratio relation
        """
        response = self.client.open(
            '/api/analytic/relation',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
