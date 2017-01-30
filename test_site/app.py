from flask import Flask
from .models import models
from flask_dstore import API
from dstore import MemoryStore


def create_app( name = __name__, config = "tests.configs.unit_tests", store = MemoryStore ):
    app = Flask( name, static_url_path = "", static_folder = "web/app" )
    app.config.from_object( config )
    api = API( store( models ), app )

    return app, api
