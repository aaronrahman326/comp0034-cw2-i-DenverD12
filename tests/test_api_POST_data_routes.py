"""This file tests the POST routes."""
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app import db

# Define Schemas
countries_schema = TourismArrivalsSchema(many=True)
country_schema = TourismArrivalsSchema()


def test_post_country_added_when_add_country(
    test_client,
    country_example_base_valid_model,
    country_example_base_valid_json,
    country_example_valid_model_with_valid_nulls,
    country_example_valid_json_with_valid_nulls,
):
    """
    Tests if a new country row is correctly posted via POST request.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.
        country_example_base_valid_model: fixture containing first test
            case - valid example model object.
        country_example_base_valid_json: fixture containing first test
            case - valid example model in JSON.
        country_example_valid_model_with_valid_nulls: fixture containing
            second test case - valid example model object with valid
            null values.
        country_example_valid_json_with_valid_nulls: fixture containing
            second test case - valid example model in JSON, with valid
            nulls.

    Given: a test client and valid country model and JSON data
    When: a country is added by making a POST request to
          "/api/countries" with the given data
    Then: the new country is added to the database and its data
          matches the given JSON data, and
          the response status code is 201, and
          the number of countries in the database increases by 1.

    """
    # Define valid test cases, explained in docstring
    test_case_dictionary = {
        country_example_base_valid_model:
        country_example_base_valid_json,
        country_example_valid_model_with_valid_nulls:
        country_example_valid_json_with_valid_nulls,
    }
    # Assign each test case example to a common variable
    for model, model_json in test_case_dictionary.items():
        country_example_model = model
        country_example_json = model_json

    # Check if the country exists, if it does then delete it
    exists = db.session.execute(
        db.select(TourismArrivals).filter_by(
            Country_Name=country_example_model.Country_Name
        )
    ).scalar()
    if exists:
        # if country does exist, then delete it
        db.session.execute(
            db.delete(TourismArrivals).where(
                TourismArrivals.Country_Name ==
                country_example_model.Country_Name
            )
        )
        db.session.commit()

    # Count the number of countries before adding a new one
    num_countries_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(TourismArrivals)
    )

    # Add the new country row via post route method
    response = test_client.post("/api/countries", json=country_example_json)
    # Count the number of countries after the new country is added
    num_countries_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(TourismArrivals)
    )
    data = response.json

    # Assert if correct expected values are in the posted entry
    for key, value in country_example_json.items():
        assert data[key] == value

    # Assert correct status code and correct count after adding
    assert response.status_code == 201
    assert num_countries_in_db_after == num_countries_in_db + 1


def test_post_country_not_added_when_invalid_entry(
    test_client,
    expected_column_value_types,
    country_example_invalid_model_with_invalid_nulls,
    country_example_invalid_json_with_invalid_nulls,
):
    """
    Test POST method for correct error response for invalid entry.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.
        expected_column_value_types: fixture (multi-use) that contains a
            dictionary of the correct expected keys/column names and the
            columns that can't be empty or null.
        country_example_invalid_model_with_invalid_nulls: fixture that
            contains a country model object with invalid null entries in
            non-nullable columns
        country_example_invalid_json_with_invalid_nulls: fixture that
            contains a country model JSON with invalid null entries in
            non-nullable columns

    Given: - A Flask test client instance of the Flask server and dictionaries
             of expected column names and the non-nullable columns.
           - A country model object and JSON with invalid null entries in
             non-nullable columns.
    When: - A POST request is made to the /api/countries endpoint with the
            invalid country model JSON.
    Then: - The server should return a 400 status code.
          - An error message should be returned indicating that the entered
            value for the IncomeGroup column cannot be empty or null.

    """
    # Define invalid test cases
    test_case_dictionary = {
        country_example_invalid_model_with_invalid_nulls:
        country_example_invalid_json_with_invalid_nulls
    }

    for model, model_json in test_case_dictionary.items():
        country_example_model = model
        country_example_json = model_json

    # Check if the country exists, if it does then delete it
    exists = db.session.execute(
        db.select(TourismArrivals).filter_by(
            Country_Name=country_example_model.Country_Name
        )
    ).scalar()
    if exists:
        # if country does exist, then delete it
        db.session.execute(
            db.delete(TourismArrivals).where(
                TourismArrivals.Country_Name ==
                country_example_model.Country_Name
            )
        )
        db.session.commit()

    expected_types, non_nullable_columns = expected_column_value_types

    # Add a new country row via post route method
    response = test_client.post("/api/countries", json=country_example_json)
    assert response.status_code == 400

    # For the first 5 columns only, the entered data cannot be null
    # Applies to test case of IncomeGroup Column entry
    for key in list(
        country_example_invalid_json_with_invalid_nulls.keys()
    )[:5]:
        if key in non_nullable_columns:
            if not country_example_invalid_json_with_invalid_nulls[key]:
                expected_error_message = {
                    "status": 400,
                    "error": str(
                        "The value entered for IncomeGroup "
                        "cannot be empty or null"
                    ),
                }
                assert ValueError(expected_error_message)
