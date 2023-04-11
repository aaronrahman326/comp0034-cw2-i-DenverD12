# import jwt
# from functools import wraps
# from datetime import datetime, timedelta
# import sys, json
from flask import (
    current_app as app,
    request,
    make_response,
    jsonify,
    Blueprint,
)

# from tourism_hotels_app.models import User
from tourism_hotels_app.utilities import get_country, get_countries, get_year
# Import created Schemas from the schemas.py
from tourism_hotels_app.schemas import TourismArrivalsSchema

# Blueprint
obtain_data_api_bp = Blueprint("api_obtain_data", __name__, url_prefix="/api")

# Schemas
# Import Marshmallow SQLAlchemy schemas and create instances of each
# First for multiple results (i.e. for all countries).
countries_schema = TourismArrivalsSchema(many=True)
# For one country
country_schema = TourismArrivalsSchema()


@obtain_data_api_bp.get("/countries")
def get_all_countries():
    """
    Returns a response that contains a list of countries and their
    international tourism details in JSON.
    Also returns status code of 200 for OK (success).
    """
    # Use helper function from utilities.py to get JSON of all countries data
    all_countries = get_countries()
    response = make_response(all_countries, 200)

    return response


@obtain_data_api_bp.get("/countries/country/<country_name>")
def by_country(country_name):
    """
    Returns a JSON response with details for a particular country.
    Also returns status code of 200 for OK (success).
    """
    country_result = get_country(country_name)
    if country_result:
        response = make_response(country_result, 200)
        response.headers["Content-Type"] = "application/json"
    else:
        message = jsonify(
            {
                "status": 404,
                "error": "Not found",
                "message": "Invalid resource URI: Invalid Country Name",
            }
        )
        response = make_response(message, 404)
    return response


@obtain_data_api_bp.get("/filterby/year/<chosen_year>")
def by_year(chosen_year):
    """
    Returns a JSON response, for a particular year column,
    returns all countries corresponding to that year column.
    Also returns status code of 200 for OK (success).
    """
    # Use helper function from utilities.py to get JSON of all countries data
    try:
        year_result = get_year(chosen_year)
        response = make_response(year_result, 200)
        response.headers["Content-Type"] = "application/json"
        return response
    except AttributeError:
        message = jsonify(
            {
                "status": 404,
                "error": "Not found",
                "message": "Invalid resource URI: Invalid year",
            }
        )
        response = make_response(message, 404)
        return response

