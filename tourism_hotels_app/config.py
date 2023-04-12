"""Flask configuration classes."""
from pathlib import Path

# Sets the project root folder
PROJECT_ROOT = Path(__file__).parent


class Config:
    """
    Base configuration class for the Flask application.

    This class defines base configuration settings for the Flask app,
    including the secret key and the path to the SQLAlchemy database.
    It is the base class that all other configuration classes inherit.

    Attributes:
        SECRET_KEY (str): A secret key used to sign session cookies
            and other secure data.
        SQLALCHEMY_DATABASE_URI (str): The URI path for the SQLite database.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Whether or not to track
            modifications to database models.
        SQLALCHEMY_ECHO (bool): Whether or not to show SQL statements for
            easier debugging.
        JSON_SORT_KEYS (bool): Whether or not to sort JSON keys.
    """

    # Define unique secret key and define URI path
    SECRET_KEY = "YY3R4fQ5OmlmVKOSlsVHew"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "tourism_hotels.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    # Disable autosort for json keys to keep desired order
    JSON_SORT_KEYS = False


class ProdConfig(Config):
    """
    Production configuration class for the Flask application.

    This class contains configuration settings for when the application is
    deployed in a production environment. It disables testing, debugging, and
    tracking features to ensure optimal performance and security.

    Attributes:
        TESTING (bool): Whether or not to enable testing mode.
        DEBUG (bool): Whether or not to enable debugging mode.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Whether or not to track
            modifications to database models.
        JSON_SORT_KEYS (bool): Whether or not to sort JSON keys.
    """

    # Disable testing, debugging and tracking
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JSON_SORT_KEYS = False
    pass


class DevelopmentConfig(Config):
    """
    Development configuration class for the Flask application.

    This class defines configuration settings for the Flask app when it
    is being developed.
    It enables debugging and testing features, and disables JSON key
    sorting, all to allow for easier development.

    Attributes:
        FLASK_ENV (str): The Flask environment, set to 'development'.
        DEBUG (bool): Whether or not to enable debugging mode.
        TESTING (bool): Whether or not to enable testing mode.
        JSON_SORT_KEYS (bool): Whether or not to sort JSON keys.
    """

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    JSON_SORT_KEYS = False


class TestConfig(Config):
    """
    Testing configuration class for the Flask application.

    This class defines configuration settings for the Flask app when
    it is being tested.
    It enables testing mode, sets the SQLAlchemy echo mode to True, and
    disables the CSRF protection for easier testing. 
    It also sets the server name and disables JSON key sorting
    for easier testing.

    Attributes:
        TESTING (bool): Whether or not to enable testing mode.
        SQLALCHEMY_ECHO (bool): Whether or not to show SQL statements
        for easier debugging.
        WTF_CSRF_ENABLED (bool): Whether or not to enable CSRF protection.
        SERVER_NAME (str): The server name to be used for the application.
        JSON_SORT_KEYS (bool): Whether or not to sort JSON keys.
    """
    TESTING = True
    SQLALCHEMY_ECHO = True
    # CSRF set to false to prevent fail during testing
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "127.0.0.1:5000"
    JSON_SORT_KEYS = False
