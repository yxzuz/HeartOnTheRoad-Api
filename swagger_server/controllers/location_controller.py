import connexion
import six

from swagger_server.models.location_trip import LocationTrip  # noqa: E501
from swagger_server import util


def get_location_trip(trip_id):  # noqa: E501
    """Get location data for a trip

     # noqa: E501

    :param trip_id: 
    :type trip_id: float

    :rtype: List[LocationTrip]
    """
    return 'do some magic!'

def get_speed_by_traffic(is_traffic_jam):  # noqa: E501
    """Get current speed data filtered by traffic condition

     # noqa: E501

    :param is_traffic_jam: 
    :type is_traffic_jam: bool

    :rtype: List[InlineResponse2008]
    """
    return 'do some magic!'
