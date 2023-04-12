# import sys
from tourism_hotels_app import db
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
import json
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify, request
from werkzeug.exceptions import BadRequest

# Marshmallow Schemas
countries_schema = TourismArrivalsSchema(many=True)
country_schema = TourismArrivalsSchema()


def get_countries():
    """Function to get all countries from the database as objects and convert to json.

    NB: This was extracted to a separate function as it is used in multiple places
    """

    all_countries = db.session.execute(db.select(TourismArrivals)).scalars()
    countries_json = countries_schema.dump(all_countries)

    return countries_json


def get_country(country_name):
    """Function to get a single event as a json structure"""

    country = db.session.execute(
        db.select(TourismArrivals).filter_by(Country_Name=country_name)
    ).scalar_one_or_none()

    if country:
        result = country_schema.dump(country)
        return result
    else:
        return country


def get_year(chosen_year):
    # Get the data from the database using SQLAlchemy

    query = TourismArrivals.query.with_entities(
        TourismArrivals.Country_Name,
        getattr(TourismArrivals, f"year_{chosen_year}"),
    ).all()
    # Create the schema to serialize the data
    country_schema_for_chosen_year = TourismArrivalsSchema(
        only=["Country_Name", f"year_{chosen_year}"], many=True
    )
    # Serialize the data to JSON
    response = country_schema_for_chosen_year.dump(query)

    return response


def create_country_format():
    data, expected_types, non_nullable_columns = get_expected_types()
    # Check that all required keys, i.e. Column names are present
    # in the JSON data
    required_keys = expected_types.keys()
    missing_keys = required_keys - data.keys()
    if missing_keys:
        raise ValueError(f"Missing required keys: {', '.join(missing_keys)}")

    # Check that the values of the keys match their expected types
    for key, expected_type in expected_types.items():
        value = data.get(key)
        if value is not None and not isinstance(value, expected_type):
            raise ValueError(
                f"The value entered for {key} should be of type: {expected_type.__name__}"
            )

    # For the first 5 columns only, the entered data cannot be null
    for key in list(data.keys())[:5]:
        if key in non_nullable_columns:
            if not data[key]:
                raise ValueError(f"The value entered for {key} cannot be empty or null")

    # If all the validation passes, create the new country format object
    new_country_format = TourismArrivals(**data)
    return new_country_format


def get_updated_country(existing_country, country_name):
    data, expected_types, non_nullable_columns = get_expected_types()
    # Check that the values of the keys match their expected types
    for key, expected_type in expected_types.items():
        value = data.get(key)
        # If entered value is not null but not the correct type, raise error
        if value is not None and not isinstance(value, expected_type):
            raise ValueError(
                f"The value entered for {key} should be of type: {expected_type.__name__}"
            )

    # For the first 5 columns only, the entered data cannot be null
    for key in list(data.keys())[:5]:
        if key in non_nullable_columns:
            if not data[key]:
                raise ValueError(f"The value entered for {key} cannot be empty or null")

    # Get the updated details from the json sent in the HTTP patch request
    country_json = request.get_json()

    # Check if any new value entered for key (entire value) already exists
    for key, value in country_json.items():
        # Strips whitespace when matching to ensure only if
        # entire value exists, to raise the error
        existing_record = getattr(existing_country, key)
        if value == existing_record:
            raise ValueError(
                f"Value entered of '{value}' for '{key}' already exists in the database"
            )

    # Update existing records with JSON changes and commit to database
    country_schema.load(country_json, instance=existing_country, partial=True)
    db.session.commit()
    # Return json showing the updated record
    updated_country = db.session.execute(
        db.select(TourismArrivals).filter_by(Country_Name=country_name)
    ).scalar_one_or_none()
    result = country_schema.jsonify(updated_country)
    return result


# -----
# Sub-Helper Functions used by Helper Functions on this page
# -----
def get_expected_types():
    # Define a dictionary with keys as column names and values as their expected data types
    expected_types = {
        "Country_Name": str,
        "Region": str,
        "IncomeGroup": str,
        "Country_Code": str,
        "Indicator_Name": str,
        "year_1995": int,
        "year_1996": int,
        "year_1997": int,
        "year_1998": int,
        "year_1999": int,
        "year_2000": int,
        "year_2001": int,
        "year_2002": int,
        "year_2003": int,
        "year_2004": int,
        "year_2005": int,
        "year_2006": int,
        "year_2007": int,
        "year_2008": int,
        "year_2009": int,
        "year_2010": int,
        "year_2011": int,
        "year_2012": int,
        "year_2013": int,
        "year_2014": int,
        "year_2015": int,
        "year_2016": int,
        "year_2017": int,
        "year_2018": int,
        "year_2019": int,
        "year_2020": int,
        "Average_10year_in_tourist_arrivals": str,
        "Max_number_of_arrivals": int,
        "Minimum_number_of_arrivals": int,
        "Percent_drop_2019_to_2020": str,
    }

    non_nullable_columns = {
        "Country_Name": str,
        "Region": str,
        "IncomeGroup": str,
        "Country_Code": str,
        "Indicator_Name": str,
    }

    # Get the JSON data from the request
    data = request.get_json()
    return data, expected_types, non_nullable_columns
