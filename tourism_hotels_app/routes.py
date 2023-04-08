# import jwt
# from functools import wraps
# from datetime import datetime, timedelta
# import sys, json
from flask import (
    render_template,
    current_app as app,
    # request,
    # make_response,
    # jsonify,
    Blueprint
)
# from tourism_hotels_app import db
# from tourism_hotels_app.models import TourismArrivals
# from tourism_hotels_app.models import User
from tourism_hotels_app.utilities import get_countries

# Import created Schemas from the schemas.py
from tourism_hotels_app.schemas import TourismArrivalsSchema

# Blueprint
main_api_bp = Blueprint('api', __name__, url_prefix="/api")

# Schemas
# Import Marshmallow SQLAlchemy schemas and create instances of each
# First for multiple results (i.e. for all countries).
arrivals_countries_schema = TourismArrivalsSchema(
    many=True
)  
# For one country
arrivals_country_schema = TourismArrivalsSchema()

# TODO: Reorgansise later maybe to create a main site blueprint file called main_site.py
# API routes
@main_api_bp.route("/api")
def index():
    """Returns the home page"""
    # The following version using a url isn't supported by the flask test client, use selenium to test it
    # url = "http://127.0.0.1:5001/event"
    # response = requests.get(url).json()

    # This version doesn't require a call to another URL so should work with the test client
    response = get_countries()
    return render_template("index.html", country_list=response)


# # API Routes
# @main_api_bp.route("/app")
# def index():
#     """Returns the home page"""
#     # The following version using a url isn't supported by the flask test client, use selenium to test it
#     # url = "http://127.0.0.1:5001/event"
#     # response = requests.get(url).json()

#     # This version doesn't require a call to another URL so should work with the test client
#     return "<h1>test<h1>"