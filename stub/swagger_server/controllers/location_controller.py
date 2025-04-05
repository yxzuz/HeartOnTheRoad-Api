import connexion
import six

from swagger_server.models.location_trip import InlineResponse2004  # noqa: E501
from swagger_server import util


def get_location_trip(trip_id):  # noqa: E501
    """Get location data for a trip

     # noqa: E501

    :param trip_id: 
    :type trip_id: float

    :rtype: List[InlineResponse2004]
    """
    return 'do some magic!'
