from flask import Flask, render_template
from .models import models
from flask_dstore import API
from dstore_mongo import MongoStore


def create_app( name = __name__, config = "tests.configs.unit_tests" ):
    app = Flask( name, static_url_path = "", static_folder = "web/app" )
    app.config.from_object( config )
    api = API( MongoStore( models ), app )

    return app, api
