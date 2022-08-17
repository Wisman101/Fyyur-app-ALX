# ---------------------------------------------------------------------------- #
# App Config.
# ---------------------------------------------------------------------------- #
from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# TODO: connect to a local postgresql database
migrate = Migrate(app, db, compare_type=True)
