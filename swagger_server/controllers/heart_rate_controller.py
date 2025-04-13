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

def get_heartrate_by_traffic(is_traffic_jam):  # noqa: E501
    """Get timestamped heart rate data filtered by traffic condition

     # noqa: E501

    :param is_traffic_jam: 
    :type is_traffic_jam: bool

    :rtype: List[InlineResponse2007]
    """
    return 'do some magic!'
