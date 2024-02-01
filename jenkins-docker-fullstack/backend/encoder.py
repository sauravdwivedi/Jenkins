from connexion.apps.flask_app import FlaskJSONEncoder
import six

from backend.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            return o.to_dict()
        return FlaskJSONEncoder.default(self, o)
