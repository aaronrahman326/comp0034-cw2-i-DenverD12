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
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from tourism_hotels_app import db
from tourism_hotels_app.models import TourismArrivals

# from tourism_hotels_app.models import User
from tourism_hotels_app.utilities import create_country_format, get_updated_country
# Import created Schemas from the schemas.py
from tourism_hotels_app.schemas import TourismArrivalsSchema

# Blueprint
update_data_api_bp = Blueprint("api_update_data", __name__, url_prefix="/api")

# Schemas
# Import Marshmallow SQLAlchemy schemas and create instances of each
# First for multiple results (i.e. for all countries).
countries_schema = TourismArrivalsSchema(many=True)
# For one country
country_schema = TourismArrivalsSchema()


@update_data_api_bp.post("/countries")
def add_country():
    """Adds a new country record with its tourism details to the dataset."""

    try:
        new_country_format = create_country_format()

        db.session.add(new_country_format)

        db.session.commit()
        result = country_schema.jsonify(new_country_format)
        response = make_response(result, 201)
        response.headers["Content-Type"] = "application/json"
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Country name already exists in the database!'}), 409
    except ValueError as error_message:
        db.session.rollback()
        custom_error_message_string = str(error_message)
        return jsonify({'error': custom_error_message_string}), 400
    return response


@update_data_api_bp.patch("/countries/<country_name>")
def edit_existing_country(country_name):
    """
    Updates an existing country record with the JSON data entered for a specific field 
    """
    try:
        # Find the current event in the database
        existing_country = db.session.execute(
            db.select(TourismArrivals).filter_by(Country_Name=country_name)
        ).scalar_one_or_none()

        if existing_country: 
            result = get_updated_country(existing_country, country_name)
            response = make_response(result, 200)
            response.headers["Content-Type"] = "application/json"
            return response
        else:
            message = jsonify(
                {
                    "status": 404,
                    "error": "Not found",
                    "message": "Invalid resource URI",
                }
            )
            response = make_response(message, 404)
            return response
    except ValueError as value_error_message:
        error_messages = str(value_error_message)
        return jsonify({'error': error_messages}), 400
    except ValidationError as validation_error_message:
        error_messages = []
        for field, errors in validation_error_message.messages.items():
            for error in errors:
                error_messages.append(f"The value you entered: {field} is: {error}")
        error_message = ", ".join(error_messages)
        return jsonify({'error': error_message}), 400
