"""File containing blueprint of routes to get data in various ways."""
from flask import (
    make_response,
    jsonify,
    Blueprint,
)
from tourism_hotels_app import db

# Import created Schemas from the schemas.py
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app.models import TourismArrivals
from sqlalchemy import desc

# Import helper functions from utilities file,
# containing error handling and major functions for routes
from tourism_hotels_app.utilities import get_country, get_countries, get_year

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
    Endpoint to get the list of countries details.

    All international tourism details returned in JSON format,
    including data from every column.
    Args:
        None

    Returns:
        response_all_countries: A JSON response object containing a
        list of countries and their international tourism details
    """
    # Use helper function from utilities.py to get JSON of all countries
    all_countries = get_countries()

    # Create a response object with JSON data and status code of 200
    response_all_countries = make_response(all_countries, 200)
    # Set the Content-Type header to application/json
    response_all_countries.headers["Content-Type"] = "application/json"
    return response_all_countries


@obtain_data_api_bp.get("/countries/country/<country_name>")
def by_country(country_name):
    """
    Return a JSON response with details for a particular country.

    Args:
        country_name(str): A string entered in the URI representing
        the name of the country to fetch data for.

    Returns:
        response: - A JSON response with details for the specified
                    country, if it exists in database.
                  - Status code of 200 for OK (success), or 404 for
                    Not Found (failure).

    Also returns status code of 200 for OK (success).

    """
    # Get data for specified country using helper in utilities.py
    country_result = get_country(country_name)

    # If the country exists, return a response with the data,
    # and a status code of 200
    if country_result:
        response = make_response(country_result, 200)
        response.headers["Content-Type"] = "application/json"
    # If the country does not exist, return a response with an error
    # message and a status code of 404
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
    Return a JSON response of all countries in the particular year.

    Args:
        chosen_year (str): The year value passed in the URI to filter
        the data by.

    Returns:
        response: - A JSON response containing all countries and their
                    details for the given year and a status code of 200
                    for OK (success).
                  - Or a error message JSON with status code of 404 for
                    not found.

    """
    try:
        # Use helper function from utilities.py to get JSON of all
        # countries data
        year_result = get_year(chosen_year)

        # Make response with year JSON data and success status code
        response = make_response(year_result, 200)
        response.headers["Content-Type"] = "application/json"
        return response
    # If an invalid year is passed, return a 404 error JSON message
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


@obtain_data_api_bp.get("/top-10-countries")
def top_countries():
    """
    Return JSON of top 10 countries with the highest average arrivals.

    Returns a JSON response containing details of top 10 countries with
    the highest average tourist arrivals in the last 10 recorded years.

    Args:
        None

    Returns:
        response: JSON response containing the names of the top 10
        countries with the highest average tourist arrivals with the
        averages.


    """
    # Get top 10 countries based on average tourist arrivals in the
    # last 10 recorded years
    top_10_countries = (
        db.session.query(
            TourismArrivals.Country_Name,
            TourismArrivals.Average_10year_in_tourist_arrivals,
        )
        .group_by(TourismArrivals.Country_Name)
        .order_by(desc(TourismArrivals.Average_10year_in_tourist_arrivals))
        .limit(10)
        .all()
    )

    # Create a dictionary with each country and its average data
    result = {"data": []}
    for country in top_10_countries:
        result["data"].append(
            {"Country_Name": country[0], "Max_number_of_arrivals": country[1]}
        )

    # Create a JSON response message of the data above
    success_message = jsonify(
        {
            "Top 10 countries for tourist arrivals": [
                {
                    "Country_Name": country_name,
                    "Average arrivals in last 10 recorded years":
                    tourist_arrivals,
                }
                for country_name, tourist_arrivals in top_10_countries
            ]
        }
    )
    response = make_response(success_message, 200)
    response.headers["Content-Type"] = "application/json"
    return response
