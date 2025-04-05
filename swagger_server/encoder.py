from connexion.apps.flask_app import FlaskJSONEncoder
import six
import datetime  # Import datetime module
from swagger_server.models.base_model_ import Model

class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in six.iteritems(o.swagger_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        elif isinstance(o, datetime.timedelta):  # Handle timedelta objects
            return round(o.total_seconds() / 60, 2)  # Convert timedelta to minutes and round
        return super().default(o)  # Use Flask's default method for other types
