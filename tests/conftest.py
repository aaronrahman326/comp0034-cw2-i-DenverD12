import pytest
from tourism_hotels_app import create_app, config
from tourism_hotels_app.models import TourismArrivals


# Define an app instance fixture for flask routes test
@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing"""
    app = create_app(config.TestConfig)
    yield app

# Define a test client fixture for flask routes test
@pytest.fixture(scope="function")
def test_client(app):
    """Create a Flask test client"""
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client