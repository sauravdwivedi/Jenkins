import logging
import os
import connexion
from flask_testing import TestCase
from backend.encoder import JSONEncoder
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openapi/", server="tornado")
        app.app.json_encoder = JSONEncoder
        app.add_api("transaction_management.json")
        app.app.instance_path = "."
        app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
        return app.app
