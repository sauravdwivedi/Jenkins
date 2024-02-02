from flask import Flask, render_template
import os
from flask_cors import CORS
import connexion
import backend.encoder as encoder
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate
from db import db

app = Flask(__name__)
connex_app = connexion.FlaskApp(
    __name__, specification_dir="./openapi/", server="tornado"
)
connex_app.add_api(
    "transaction_management.json",
    arguments={"title": "Transaction Management API"},
    pythonic_params=True,
    validate_responses=True,
    base_path="/api/v1",
)
app = connex_app.app
app.json_encoder = encoder.JSONEncoder
CORS(app)
app.instance_path = "."
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["DATABASE"] = os.path.join(app.instance_path, "backend.sqlite")

if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    create_database(app.config["SQLALCHEMY_DATABASE_URI"])

db.init_app(app)
migrate = Migrate(app, db)
