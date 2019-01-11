from flask import Flask

from instance.config import app_config
from .api.v1.views.meetups_endpoints import meetup


def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(meetup)
    app.config.from_object(app_config[config])
    return app
