# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TripDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, record: object=None, start_time: datetime=None, duration: float=None, min_heartrate: float=None, max_heartrate: float=None, average_heartrate: float=None):  # noqa: E501
        """TripDetails - a model defined in Swagger

        :param record: The record of this TripDetails.  # noqa: E501
        :type record: object
        :param start_time: The start_time of this TripDetails.  # noqa: E501
        :type start_time: datetime
        :param duration: The duration of this TripDetails.  # noqa: E501
        :type duration: float
        :param min_heartrate: The min_heartrate of this TripDetails.  # noqa: E501
        :type min_heartrate: float
        :param max_heartrate: The max_heartrate of this TripDetails.  # noqa: E501
        :type max_heartrate: float
        :param average_heartrate: The average_heartrate of this TripDetails.  # noqa: E501
        :type average_heartrate: float
        """
        self.swagger_types = {
            'record': object,
            'start_time': datetime,
            'duration': float,
            'min_heartrate': float,
            'max_heartrate': float,
            'average_heartrate': float
        }

        self.attribute_map = {
            'record': 'record',
            'start_time': 'start_time',
            'duration': 'duration',
            'min_heartrate': 'min_heartrate',
            'max_heartrate': 'max_heartrate',
            'average_heartrate': 'average_heartrate'
        }
        self._record = record
        self._start_time = start_time
        self._duration = duration
        self._min_heartrate = min_heartrate
        self._max_heartrate = max_heartrate
        self._average_heartrate = average_heartrate

    @classmethod
    def from_dict(cls, dikt) -> 'TripDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this TripDetails.  # noqa: E501
        :rtype: TripDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def record(self) -> object:
        """Gets the record of this TripDetails.


        :return: The record of this TripDetails.
        :rtype: object
        """
        return self._record

    @record.setter
    def record(self, record: object):
        """Sets the record of this TripDetails.


        :param record: The record of this TripDetails.
        :type record: object
        """

        self._record = record

    @property
    def start_time(self) -> datetime:
        """Gets the start_time of this TripDetails.


        :return: The start_time of this TripDetails.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        """Sets the start_time of this TripDetails.


        :param start_time: The start_time of this TripDetails.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def duration(self) -> float:
        """Gets the duration of this TripDetails.

        Duration in minutes  # noqa: E501

        :return: The duration of this TripDetails.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        """Sets the duration of this TripDetails.

        Duration in minutes  # noqa: E501

        :param duration: The duration of this TripDetails.
        :type duration: float
        """

        self._duration = duration

    @property
    def min_heartrate(self) -> float:
        """Gets the min_heartrate of this TripDetails.


        :return: The min_heartrate of this TripDetails.
        :rtype: float
        """
        return self._min_heartrate

    @min_heartrate.setter
    def min_heartrate(self, min_heartrate: float):
        """Sets the min_heartrate of this TripDetails.


        :param min_heartrate: The min_heartrate of this TripDetails.
        :type min_heartrate: float
        """

        self._min_heartrate = min_heartrate

    @property
    def max_heartrate(self) -> float:
        """Gets the max_heartrate of this TripDetails.


        :return: The max_heartrate of this TripDetails.
        :rtype: float
        """
        return self._max_heartrate

    @max_heartrate.setter
    def max_heartrate(self, max_heartrate: float):
        """Sets the max_heartrate of this TripDetails.


        :param max_heartrate: The max_heartrate of this TripDetails.
        :type max_heartrate: float
        """

        self._max_heartrate = max_heartrate

    @property
    def average_heartrate(self) -> float:
        """Gets the average_heartrate of this TripDetails.


        :return: The average_heartrate of this TripDetails.
        :rtype: float
        """
        return self._average_heartrate

    @average_heartrate.setter
    def average_heartrate(self, average_heartrate: float):
        """Sets the average_heartrate of this TripDetails.


        :param average_heartrate: The average_heartrate of this TripDetails.
        :type average_heartrate: float
        """

        self._average_heartrate = average_heartrate
