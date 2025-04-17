import connexion
import six

from swagger_server.models.analytic_data import AnalyticData  # noqa: E501
from swagger_server.models.analytic_relation import AnalyticRelation  # noqa: E501
from swagger_server import util


def get_analytic_data():  # noqa: E501
    """Get analytics data

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_analytic_relation():  # noqa: E501
    """Get heart rate and traffic ratio relation

     # noqa: E501


    :rtype: List[InlineResponse2001]
    """
    return 'do some magic!'
