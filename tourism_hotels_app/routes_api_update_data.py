"""File containing blueprint of routes to post and patch data in RESTAPI."""
from flask import make_response, jsonify, Blueprint
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest
from tourism_hotels_app import db
from tourism_hotels_app.models import TourismArrivals

# Import helper functions from utilities file,
# containing error handling and major functions for routes
from tourism_hotels_app.utilities import (
    create_country_format,
    get_updated_country
)

# Import created Schemas from the schemas.py
from tourism_hotels_app.schemas import TourismArrivalsSchema

# Blueprint
update_data_api_bp = Blueprint("api_update_data", __name__, url_prefix="/api")

# Schemas
# Import Marshmallow SQLAlchemy schemas and create instances of each
# Create instance for multiple results (i.e. for many/all countries).
countries_schema = TourismArrivalsSchema(many=True)
# Create instance for one country
country_schema = TourismArrivalsSchema()


@update_data_api_bp.post("/countries")
def add_country():
    """
    Add a new country record with its tourism details to the dataset.

    Args:
        None

    Returns:
        response: A Flask response object which updates database with
        the new country row and returns appropriate HTTP status code
        and content type or relevant error message.

    Raises:
        BadRequest: If any word or text entered is not a string.
        ValueError: Three possible cases of value error defined in
        utilities.py.
        AttributeError: If any of the input keys do not match the
        expected column names.
    """
    try:
        # Use helper function from utilties.py to attempt to create a
        # new country based on request JSON body entered
        new_country_format = create_country_format()
        # Add new country row to database and commit changes
        db.session.add(new_country_format)
        db.session.commit()

        # Make the JSON response of the successful post with status code
        result = country_schema.jsonify(new_country_format)
        response = make_response(result, 201)
        response.headers["Content-Type"] = "application/json"
    # Catch error if the Country_Name key's value already exists
    except IntegrityError:
        # Rollback session to undo changes, if error
        # and raise JSON message with status code
        db.session.rollback()
        # Create JSON message response with status code 409
        message = jsonify(
            {
                "status": 409,
                "error": "Database Integrity Error",
                "message": "Country name already exists in the database!",
            }
        )
        response = make_response(message, 409)
        response.headers["Content-Type"] = "application/json"
    # Catch the 3 types of value error custom message defined in
    # helper function get_updated_country()
    except ValueError as error_message:
        # Rollback session and raise JSON message with status code
        db.session.rollback()
        custom_error_message_json = jsonify(
            {
                "status": 400,
                "error": str(error_message)
            }
        )
        response = make_response(custom_error_message_json, 400)
        response.headers["Content-Type"] = "application/json"
    # Catch Attribute error called from helper function above
    # to indicate key(database column) name entered does not exist
    except AttributeError:
        # Rollback session and raise JSON message with status code
        db.session.rollback()
        error_message_json = jsonify(
            {
                "status": 404,
                "error": "Invalid key entry: "
                "That column name does not exist.",
            }
        )
        response = make_response(error_message_json, 400)
        response.headers["Content-Type"] = "application/json"
    # Catch the BadRequest error if any value entered is a word or text but
    # without quotes like a proper string.
    except BadRequest as badrequest_message:
        # Rollback session and raise JSON message with status code
        db.session.rollback()
        badrequest_message = (
            "The value entered for the key was in the wrong format or was a "
            "string/text entered without being wrapped in quotes."
        )
        error_message_json = jsonify(
            {
                "status": 400,
                "error": "Bad Request",
                "message": badrequest_message,
            }
        )
        response = make_response(error_message_json, 400)
        response.headers["Content-Type"] = "application/json"
    return response


@update_data_api_bp.patch("/countries/<country_name>")
def edit_existing_country(country_name):
    """
    Update existing country record with new JSON data for any fields.

    Args:
        country_name (str): The name of the country to update passed
        in URI

    Returns:
        response: A Flask response containing JSON data of either
        the updated record or an error message.

    Raises:
        ValueError: When the helper function get_updated_country()
        raises a ValueError, defined further in the utilities.py file.
        AttributeError: When an invalid column name is entered.
        ValidationError: When the entered data is invalid for a specific
        column.
        BadRequest: When an entered text or word is not a string.
    """
    try:
        # Find the country already in the database
        existing_country = db.session.execute(
            db.select(TourismArrivals).filter_by(Country_Name=country_name)
        ).scalar_one_or_none()
        # If it exists, make a successful PATCH response of new data
        if existing_country:
            result = get_updated_country(existing_country, country_name)
            response = make_response(result, 200)
            response.headers["Content-Type"] = "application/json"
            return response
        # If country name doesn't exist, send response in JSON
        else:
            # Create JSON error message and add status code
            message = jsonify(
                {
                    "status": 404,
                    "error": "Not found",
                    "message": "Invalid resource URI - "
                               "That country does not exist",
                }
            )
            response = make_response(message, 404)
            response.headers["Content-Type"] = "application/json"
            return response

    # Returns the 3 types of value error custom message defined in
    # helper function get_updated_country()
    except ValueError as value_error_message:
        # Rollback session and raise JSON message with status code
        db.session.rollback()
        error_message_json = jsonify(
            {
                    "status": 400,
                    "error": str(value_error_message)
            }
        )
        response = make_response(error_message_json, 400)
        response.headers["Content-Type"] = "application/json"
    # Catch attribute error for non-existing key(column) entry
    except AttributeError:
        # Rollback session and raise JSON message with status code
        db.session.rollback()
        error_message_json = jsonify(
            {
                "status": 404,
                "error": "Invalid key entry: "
                "That column name does not exist.",
            }
        )
        response = make_response(error_message_json, 400)
        response.headers["Content-Type"] = "application/json"
    # Catch the ValidationError, custom message and modifies message
    except ValidationError as validation_error_message:
        # Rollback session and raise JSON message with status code
        db.session.rollback()
        # Catch custom message and send with more meaningful info
        error_messages = []
        for field, errors in validation_error_message.messages.items():
            for error in errors:
                error_messages.append(
                    f"The value entered: {field} is: {error}"
                )
        error_message_json = jsonify(
            {
                "status": 400,
                "error": ", ".join(error_messages),
             }
        )
        response = make_response(error_message_json, 400)
        response.headers["Content-Type"] = "application/json"
    # Catch the BadRequest error if any word or text entered is not a string
    except BadRequest as badrequest_message:
        # Rollback session and raise JSON message with status code
        db.session.rollback()
        badrequest_message = (
            "Bad request - The value entered for the key was in the "
            "wrong format or was a string/text entered without being "
            "wrapped in quotes."
        )
        error_message_json = jsonify({"error": badrequest_message})
        response = make_response(error_message_json, 400)
        response.headers["Content-Type"] = "application/json"
    return response
