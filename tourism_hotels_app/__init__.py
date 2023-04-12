"""Main file that handles main app functions and initializing."""
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Sets the project root folder
PROJECT_ROOT = Path(__file__).parent

# Create a global SQLAlchemy object
db = SQLAlchemy()
# Create a global Flask-Marshmallow object
ma = Marshmallow()


def create_app(config_object):
    """
    Create and configure the Flask app, connecting to the config file.

    Also initializes and registers all blueprints with routes and
    includes routes and models within app context to access request
    and app specific data.

    Args:
        config_object: Config classes from config.py

    Returns:
        app: The main flask app instance
    """
    app = Flask(__name__)
    # See config parameters in config.py, using classes
    app.config.from_object(config_object)

    # Uses a helper function to initialise extensions
    initialize_extensions(app)

    # Include the blueprints of routes for html and api
    from tourism_hotels_app.routes_html_display import html_display_bp
    from tourism_hotels_app.routes_api_obtain_data import obtain_data_api_bp
    from tourism_hotels_app.routes_api_update_data import update_data_api_bp

    # Register all blueprints
    app.register_blueprint(html_display_bp)
    app.register_blueprint(obtain_data_api_bp)
    app.register_blueprint(update_data_api_bp)

    # Include the routes within app context
    with app.app_context():
        from tourism_hotels_app import (
            routes_html_display,
            routes_api_obtain_data,
            routes_api_update_data,
        )
        # Instantiate TourismArrivals models marshamallow schemas
        from tourism_hotels_app.models import TourismArrivals

    return app


def initialize_extensions(app):
    """
    Bind extensions to the Flask application instance (app).

    Args:
        app: Flask app application instance
    Returns:
        None
    """
    # Initialize Flask-SQLAlchemy Flask-Marshmallow
    db.init_app(app)
    ma.init_app(app)
