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
from tourism_hotels_app import db, ma
# Import created Schemas from the schemas.py
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app.models import TourismArrivals
from sqlalchemy import desc

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
    response.headers["Content-Type"] = "application/json"
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
        response.headers["Content-Type"] = "application/json"
    return response


@obtain_data_api_bp.get("/filterby/year/<chosen_year>")
def by_year(chosen_year):
    """
    Returns a JSON response, for a particular year column,
    returns all countries corresponding to that year column.
    Also returns status code of 200 for OK (success).
    """

    try:
        # Use helper function from utilities.py to get JSON of all
        # countries data
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
        response.headers["Content-Type"] = "application/json"
        return response


@obtain_data_api_bp.get('/top-10-countries')
def top_countries():
    top_10_countries = db.session.query(
        TourismArrivals.Country_Name,
        TourismArrivals.Average_10year_in_tourist_arrivals,
    ).group_by(TourismArrivals.Country_Name).order_by(
        desc(TourismArrivals.Average_10year_in_tourist_arrivals)
    ).limit(10).all()

    result = {"data": []}
    for country in top_10_countries:
        result["data"].append({"Country_Name": country[0], "Max_number_of_arrivals": country[1]})

    response = jsonify(
        {
            'Top 10 countries for tourist arrivals': [{
                'Country_Name': country_name,
                'Average arrivals in last 10 recorded years': tourist_arrivals
            } for country_name, tourist_arrivals in top_10_countries]
        }
    )
    response.headers["Content-Type"] = "application/json"

    return response


# @obtain_data_api_bp.get("/top-10-countries")
# def top_10_countries_2020():
    # results = (
    #     db.session.query(
    #         TourismArrivals.Country_Name,
    #         TourismArrivals.year_2020
    #     )
    #     .order_by(TourismArrivals.year_2020.desc())
    #     .limit(10)
    #     .all()
    # )
    # top_10_countries = {
    #     'Top 10 countries for tourist arrivals': [{
    #         'Country_Name': country_name,
    #         'Average arrivals in last 10 recorded years': tourist_arrivals
    #     } for country_name, tourist_arrivals in results]
    # }

    # response = make_response(top_10_countries, 200)
    # response.headers["Content-Type"] = "application/json"
    # return response