# import jwt
# from functools import wraps
# from datetime import datetime, timedelta
# import sys, json
from flask import (
    abort,
    render_template,
    current_app as app,
    # request,
    make_response,
    jsonify,
    Blueprint,
)
from tourism_hotels_app import db
from tourism_hotels_app.models import TourismArrivals
# from tourism_hotels_app.models import User
from tourism_hotels_app.utilities import get_country, get_countries

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

@main_api_bp.get("/all_countries")
def index():
    """
    Returns a response that contains a list of countries and their
    international tourism details in JSON.
    Also returns status code of 200 for OK (success).
    """
    # Use helper function from utilities.py to get JSON of all countries data
    all_countries = get_countries()
    response = make_response(all_countries, 200)
    return response


# @main_api_bp.get("/<country_name>")
# def noc(country_name):
#     """
#     Returns a JSON response with details for a particular country.
#     Also returns status code of 200 for OK (success).
#     """

#     if country_name:
#         result = get_country(country_name)
#         response = make_response(result, 200)
#         response.headers["Content-Type"] = "application/json"
#     else:
#         message = jsonify(
#             {
#                 "status": 404,
#                 "error": "Not found",
#                 "message": "Invalid resource URI",
#             }
#         )
#         response = make_response(message, 404)
#     return response


@main_api_bp.get("/country/<country_name>")
def event_id(country_name):
    """Returns the details for a specified event"""
    result = get_country(country_name)
    response = make_response(result, 200)
    response.headers["Content-Type"] = "application/json"
    return response