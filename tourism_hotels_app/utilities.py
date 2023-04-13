"""File containing various helper functions used in all route blueprints."""
from tourism_hotels_app import db
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from flask import request

# Schemas
# Import Marshmallow schemas and create instances of each
# Create instance for multiple results (i.e. for many/all countries).
countries_schema = TourismArrivalsSchema(many=True)
# Create instance for one country
country_schema = TourismArrivalsSchema()


def get_countries():
    """
    Get all countries and convert to JSON - helper function.

    Gets all country rows from the database as objects
    and converts to json.

    Args:
        None
    Returns:
        countries_json: A JSON representation of all countries
        and their international tourism details.
    """
    # Use SQLAlchemy to execute a SELECT query on 'TourismArrivals'
    # table and get all rows as object
    all_countries = db.session.execute(db.select(TourismArrivals)).scalars()

    # Use Marshmallow to convert the objects to JSON format
    countries_json = countries_schema.dump(all_countries)
    return countries_json


def get_country(country_name):
    """
    Get data for a single country by name - helper function.

    Args:
        country_name (str): The name of the country submitted in the
        URI to retrieve data.

    Returns:
        country_result_json: A JSON representation of data for the
        requested country.
        none_result: None if the country is not found in the database.
    """
    # Use SQLalchemy to query the database for the requested country
    country = db.session.execute(
        db.select(TourismArrivals).filter_by(Country_Name=country_name)
    ).scalar_one_or_none()

    # If country is found in database,
    # Use Marshmallow to convert the objects to JSON format
    if country:
        country_result_json = country_schema.dump(country)
        return country_result_json
    # If the country is not found in the database, return None
    else:
        none_result = country
        return none_result


def get_year(chosen_year):
    """
    Get a list of all countries for a given year.

    Gets all countries and international tourism details for
    the given year in JSON.

    Args:
        chosen_year: The chosen year from URI to get tourism data.
    Returns:
        year_data_json: A JSON representation of data for the
        requested yer.
    """
    # Get the data from the database using SQLAlchemy
    query = TourismArrivals.query.with_entities(
        TourismArrivals.Country_Name,
        getattr(TourismArrivals, f"year_{chosen_year}"),
    ).all()
    # Create the schema for chosen year to serialize the data
    country_schema_for_chosen_year = TourismArrivalsSchema(
        only=["Country_Name", f"year_{chosen_year}"], many=True
    )
    # Serialize the data to JSON using Marshmallow
    year_data_json = country_schema_for_chosen_year.dump(query)
    return year_data_json


def create_country_format():
    """
    Create a new instance of TourismArrivals country with provided data.

    Validates that the provided data conforms to the expected data
    types and that all required fields are present and not null.

    Args:
        None

    Returns:
        new_country_format: A new instance of the TourismArrivals class.

    Raises:
        AttributeError: If a column/key name provided in the JSON data
        does not match the expected column/key names.
        ValueError: If any of the following validation checks fails:
            - A required key/column name is missing from the JSON data.
            - The value for a key/column name does not match its
              expected data type, defined in sub-helper function.
            - A value is null or empty for a non-nullable key/column name.

    """
    # Call helper function to get expected keys, data types
    # Also get current json response
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
                f"The value entered for {key} should be of type: "
                f"{expected_type.__name__}"
            )

    # For the first 5 columns only, the entered data cannot be null
    for key in list(data.keys())[:5]:
        if key in non_nullable_columns:
            if not data[key]:
                raise ValueError(f"The value entered for {key} "
                                 f"cannot be empty or null")

    # If all the validation passes, create the new country format object
    new_country_format = TourismArrivals(**data)
    return new_country_format


def get_updated_country(existing_country, country_name):
    """
    Update an existing country record in database with HTTP PATCH.

    With the JSON data sent in the HTTP PATCH request, updates
    the existing country if it exists.

    Args:
        existing_country: The existing country record to be updated.
        country_name (str): The name of the country to be updated.

    Returns:
        updated_result_json: A JSON string representing the updated
        country record.

    Raises:
        AttributeError: If a column/key name does not exist in the
        database.
        ValueError: - If a value entered for a key is not of the
                      expected type.
                    - If a value entered for a non-nullable key
                      is empty or null,
                    - If a new value entered for a key already
                      exists in the database.

    """
    data, expected_types, non_nullable_columns = get_expected_types()
    # Check that column/key name actually exists first
    for key in list(data.keys()):
        if key not in expected_types:
            raise AttributeError

    # Check that the values of the keys match their expected types
    for key, expected_type in expected_types.items():
        value = data.get(key)
        # If entered value is not null but not the correct type, raise error
        if value is not None and not isinstance(value, expected_type):
            raise ValueError(
                f"The value entered for {key} should be of type: "
                f"{expected_type.__name__}"
            )

    # For the first 5 columns only, the entered data cannot be null
    for key in list(data.keys())[:5]:
        if key in non_nullable_columns:
            if not data[key]:
                raise ValueError(f"The value entered for {key} "
                                 "cannot be empty or null")

    # Get the updated details from the json sent in the HTTP patch request
    country_json = request.get_json()

    # Check if any new value entered for key (entire value) already exists
    for key, value in country_json.items():
        # Strips whitespace when matching to ensure only if
        # entire value exists, to raise the error
        existing_record = getattr(existing_country, key)
        if value == existing_record:
            raise ValueError(
                f"Value entered of '{value}' for '{key}' "
                "already exists in the database"
            )

    # Update existing records with JSON changes and commit to database
    country_schema.load(country_json, instance=existing_country, partial=True)
    db.session.commit()
    # Return json showing the updated record
    updated_country = db.session.execute(
        db.select(TourismArrivals).filter_by(Country_Name=country_name)
    ).scalar_one_or_none()
    updated_result_json = country_schema.jsonify(updated_country)

    return updated_result_json


# -----
# Sub-Helper Functions used by Helper Functions on this page
# -----
def get_expected_types():
    """
    Sub-helper function.

    Gets expected correct column names and their data types,
    according to what they should be when creating the database
    and defining SQLA models and schemas.
    Also gets the non-nullable columns as defined in the models
    and schemas in the relevant files, as well as JSON data of the
    current request.

    Args:
        None
    Returns:
        expected_types_dict: A dictionary of the expected column names
        and data types they should be.
        non_nullable_columns: A dictionary containing the columns that
        cannot be null.
        current_request_data_json: JSON data of the current request
    """
    # Define a dictionary with keys as column names
    # The dictionary values are the column's expected data types
    expected_types_dict = {
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

    # Define the columns that can't be null and their data types
    non_nullable_columns = {
        "Country_Name": str,
        "Region": str,
        "IncomeGroup": str,
        "Country_Code": str,
        "Indicator_Name": str,
    }

    # Get the JSON data from the current request
    current_request_data_json = request.get_json()
    return current_request_data_json, expected_types_dict, non_nullable_columns
