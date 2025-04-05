import connexion
import six

from swagger_server.models.trip_details import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server import util


def get_number_of_trips():  # noqa: E501
    """Get number of trips

     # noqa: E501


    :rtype: InlineResponse2005
    """
    return 'do some magic!'


def get_trip_details(trip_id):  # noqa: E501
    """Get trip details

     # noqa: E501

    :param trip_id: 
    :type trip_id: float

    :rtype: InlineResponse2002
    """
    return 'do some magic!'
