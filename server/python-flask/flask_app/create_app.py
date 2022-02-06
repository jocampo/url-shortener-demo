import os

from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

from config import DATABASE_URL


def create_app(is_testing_context: bool = False):
    if "DATABASE_URL" in os.environ:
        db_url = os.environ["DATABASE_URL"]
    else:
        os.environ["DATABASE_URL"] = DATABASE_URL
        db_url = DATABASE_URL

    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.url_map.strict_slashes = False

    if is_testing_context:
        app.config["TESTING"] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    api = Api(app)
    CORS(app, support_credentials=True)

    # connection_manager = ConnectionManager(db_url)
    # session = flask_scoped_session(connection_manager.get_session_factory(), app)

    @app.route("/")
    def index():
        return render_template("index.html")

    # Register routes for the API, binding a controller to each route
    # from api.controllers.x import x
    #
    # api.add_resource(x, Routes.x.value)

    return app
