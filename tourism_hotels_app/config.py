"""Flask configuration."""
from pathlib import Path

# Sets the project root folder
PROJECT_ROOT = Path(__file__).parent


class Config:
    """Base config class with secret key and SQLAlchemy database path."""

    SECRET_KEY = "YY3R4fQ5OmlmVKOSlsVHew"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(
        PROJECT_ROOT.joinpath("data", "tourism_hotels.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    # Disable autosort for json keys to keep desired order
    JSON_SORT_KEYS = False


class ProdConfig(Config):
    """Production config.

    Not currently implemented.
    """

    pass


class DevelopmentConfig(Config):
    """Development config."""

    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    JSON_SORT_KEYS = False


class TestConfig(Config):
    """Testing config."""

    TESTING = True
    SQLALCHEMY_ECHO = True
    # CSRF set to false to prevent fail during testing
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "127.0.0.1:5000"
    JSON_SORT_KEYS = False
