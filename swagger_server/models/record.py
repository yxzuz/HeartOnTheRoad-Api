# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util

class Record(Model):
    """Record model containing total, traffic jam count, and normal count."""

    def __init__(self, total: int = 0, trafficjam: int = 0, normal: int = 0):  # noqa: E501
        """Record - a model defined in Swagger

        :param total: The total number of trips.
        :type total: int
        :param trafficjam: The number of trips with traffic jams.
        :type trafficjam: int
        :param normal: The number of normal trips.
        :type normal: int
        """
        self.swagger_types = {
            'total': int,
            'trafficjam': int,
            'normal': int
        }

        self.attribute_map = {
            'total': 'total',
            'trafficjam': 'trafficjam',
            'normal': 'normal'
        }

        self._total = total
        self._trafficjam = trafficjam
        self._normal = normal

    @classmethod
    def from_dict(cls, dikt) -> 'Record':
        """Returns the dict as a model."""
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> int:
        return self._total

    @total.setter
    def total(self, total: int):
        self._total = total

    @property
    def trafficjam(self) -> int:
        return self._trafficjam

    @trafficjam.setter
    def trafficjam(self, trafficjam: int):
        self._trafficjam = trafficjam

    @property
    def normal(self) -> int:
        return self._normal

    @normal.setter
    def normal(self, normal: int):
        self._normal = normal
