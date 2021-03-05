from flask import Flask, Blueprint

from .api.v1 import version_one as v1
from .db_con import database_setup


def create_app():
    app = Flask(__name__)
    database = database_setup()
    database.create_tables()
    app.register_blueprint(v1)

    return app
