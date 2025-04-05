import connexion
import six

from swagger_server.models.heart_rate_trip import InlineResponse2003  # noqa: E501
from swagger_server import util


def get_heart_rate_trip(trip_id):  # noqa: E501
    """Get heart rate data for a trip

     # noqa: E501

    :param trip_id: 
    :type trip_id: float

    :rtype: List[InlineResponse2003]
    """
    return 'do some magic!'
