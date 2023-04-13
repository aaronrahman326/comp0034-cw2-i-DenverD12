"""This file tests the PATCH routes."""
import pytest
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app import db

# Define Schemas
countries_schema = TourismArrivalsSchema(many=True)
country_schema = TourismArrivalsSchema()


@pytest.mark.parametrize(
    "country_name, example_valid_field_entries",
    [
        ("India", {"year_1995": 1000, "year_1996": 1500}),
        (
            "TestCountry_2",
            {"Region": "UpdatedRegion", "IncomeGroup": "UpdatedIncomeGroup"},
        ),
    ],
)
def test_edit_existing_country_with_valid_input(
    test_client, country_name, example_valid_field_entries
):
    """
    This function tests for two parametrized tests of country names.

    One if for a Country Name that already exists in the database,
    And another for a custom (mock) country name that is first added
    to the database.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.
        country_name: parameter containing valid (existing) and invalid
            (non-existent) country names test cases.
        example_valid_field_entries: parameter containing valid field
            entries other than country name, in case the name is valid.

    Given: A Flask test client,
    When: A valid country name and field entries are provided to the API
          to update an existing country,
    Then: The API should update the country's fields in the database and
          return a 200 status code.
    """
    # If the test is for custom TestCountry,
    # Create the necessary data in the database
    if country_name == "TestCountry_2":
        existing_country = TourismArrivals(
            Country_Name=country_name,
            Region="TestRegion",
            IncomeGroup="TestIncomeGroup",
            Country_Code="TestCountryCode",
            Indicator_Name="TestIndicatorName",
            year_1995=100,
            year_1996=200,
            year_1997=300,
        )
        db.session.add(existing_country)
        db.session.commit()
        data = example_valid_field_entries
    else:
        data = example_valid_field_entries

    # Make the API request
    response = test_client.patch(f"/api/countries/{country_name}", json=data)

    # Assertion success common to all valid cases
    assert response.status_code == 200

    # Get the updated country data from the database
    updated_country = (
        db.session.query(TourismArrivals).filter_by(
            Country_Name=country_name
        ).first()
    )
    # Check if all the fields in the request are updated in the database
    for key, value in data.items():
        assert getattr(updated_country, key) == value

    # Assertions specific to India test case
    if country_name == "India":
        assert "Country_Name" in updated_country.__dict__.keys()
        assert updated_country.Country_Name == "India"
        assert "year_1995" in updated_country.__dict__.keys()
        assert updated_country.year_1995 == 1000
        assert "year_1996" in updated_country.__dict__.keys()
        assert updated_country.year_1996 == 1500

    # Assertions specific to TestCountry test case
    if country_name == "TestCountry_2":
        # Check if Region, IncomeGroup fields are updated in database
        assert updated_country.Region == data["Region"]
        assert updated_country.IncomeGroup == data["IncomeGroup"]


@pytest.mark.parametrize(
    "country_name, example_entries, expected_status, expected_error",
    [
        (
            "Invalid Country",
            {"year_1995": 1000, "year_1996": 1500},
            404,
            "Not found",
        ),
        (
            "India",
            {"year_1995": "Example invalid string which should be integer"},
            400,
            "The value entered for year_1995 should be of type: int",
        ),
    ],
)
def test_edit_country_with_invalid_country_or_invalid_json_entry(
    test_client, country_name, example_entries, expected_status, expected_error
):
    """
    Test GET method with invalid country name or invalid json for year column.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.
        country_name: parameter containing invalid (non-existent) and valid
            (existing) country names test cases.
        example_entries: parameter containing valid and invalid entries for
            year columns with invalid data type.
        expected_status: parameter containing expected custom error status
            code.
        expected_error: parameter containing expected custom error status
            message.

    Given: a Flask test client and invalid country name or invalid JSON entry
    When: the /api/countries/<country_name> endpoint is patched with example
          entries
    Then: The response status code should match the expected status code, and
          the response data's 'status' field should match the expected status
          code and the response data's 'error' field should match the expected
          error message.
    """
    # Make a PATCH request to the API with each set of data
    response = test_client.patch(
        f"/api/countries/{country_name}",
        json=example_entries,
    )
    data = response.get_json()

    # Assertions of expected error status code and messages
    assert response.status_code == expected_status
    assert data["status"] == expected_status
    assert data["error"] == expected_error


def test_edit_existing_country_with_empty_payload(test_client):
    """
    Test PATCH method with with empty value entered.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.

    Given: A Flask test client.
    When: A HTTP PATCH request is made to update an existing country
          with an empty payload,
    Then: the API should return a 400 error with correct expected
          custom error message.
    """
    # Test data example existing country
    country_name = "India"
    # Example empty JSON entry for existing column name
    empty_json_entry = {"Region": ""}

    # Make a PATCH request to the API
    response = test_client.patch(
        f"/api/countries/{country_name}",
        json=empty_json_entry
    )

    # Assert the correct status code, error type and message
    assert response.status_code == 400
    assert ValueError("The value entered for Region cannot be empty or null")


def test_edit_nonexistent_country(test_client):
    """
    Test PATCH method with with non-existent country name.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.

    Given: A Flask test client.
    When: A HTTP PATCH request is made to attempt to update a country,
          who's name does not exist in the existing keys.
    Then: the API should return a 400 error with correct expected
          custom error message.
    """
    # Define a country name that does not exist in database
    country_name = "NonexistentCountry"
    # Define other acceptable data
    data = {"Region": "TestRegion", "IncomeGroup": "TestIncomeGroup"}

    # Make a PATCH request to the API and get JSON of error message
    response = test_client.patch(f"/api/countries/{country_name}", json=data)
    response_json = response.get_json()

    # Assert correct error status code and messages
    assert response.status_code == 404
    assert response_json["error"] == "Not found"
    assert (
        response_json["message"] ==
        "Invalid resource URI - That country does not exist"
    )
