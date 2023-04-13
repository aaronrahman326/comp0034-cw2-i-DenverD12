"""This file contains tests for all GET routes."""
import pytest
import json
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app import db
from urllib.error import HTTPError

# Define Schemas
countries_schema = TourismArrivalsSchema(many=True)
country_schema = TourismArrivalsSchema()


def test_get_all_countries(test_client, expected_column_value_types):
    """
    Test if GET request for countries returns correct list of countries.

    Args:
        test_client: fixture containing test client instance of app, to
        allow the tests to interact with the Flask server.
        expected_column_value_types: fixture (multi-use) that contains
        a dictionary of the correct expected keys/column names.

    Given: A Flask app configured for testing, with expected column
           names.
    When: A HTTP GET request is made to RESTAPI `/countries` endpoint.
    Then: - The response status code should be 200.
          - The response should not be empty.
          - Each item in the response should have the expected keys.
    """
    # Make a GET request to the `/countries` endpoint
    response = test_client.get("/api/countries")

    assert response.status_code == 200

    # Deserialize the response content to a Python list
    response_data = json.loads(response.data)

    # Assert that the response is not empty
    assert len(response_data) > 0

    # Define expected keys from the created fixture
    expected_keys_dict, non_nullable_columns = expected_column_value_types

    # Assert that each item in the response has the expected keys
    for country_data in response_data:
        assert set(country_data.keys()) == expected_keys_dict.keys()


@pytest.mark.parametrize(
    (
        "expected_result_cname",
        "expected_result_year2001",
        "expected_result_max",
        "expected_result_ccode",
    ),
    (
        (
            # Valid parameters
            "Aruba",
            1178000,
            1951000,
            "ABW",
        ),
        (
            # Valid parameters
            "Zimbabwe",
            2217000,
            2580000,
            "ZWE",
        ),
        (
            # Valid parameters
            "India",
            2537000,
            17914000,
            "IND",
        ),
        (
            # Invalid parameters
            "Invalid_Country",
            None,
            None,
            None,
        ),
    ),
)
def test_when_get_specific_country_then_correct_json_returned(
    test_client,
    expected_column_value_types,
    expected_result_cname,
    expected_result_year2001,
    expected_result_max,
    expected_result_ccode,
):
    """
    Test if a GET request is made for a particular country row.

    The test uses parametrize to check 2 valid test cases and 1
    invalid test case with invalid country name, "Invalid_Country".
    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.
        expected_column_value_types: fixture (multi-use) that contains a
            dictionary of the correct expected keys/column names and the
        columns that can't be empty or null.
            expected_result_cname: parameter that contains 3 example
            country names test cases, 2 valid and 1 invalid.
        expected_result_year2001: parameter containing 3 example country
            test values for year 2001.
        expected_result_max: parameter containing 3 example country
            test values for the max arrivals value per country.
        expected_result_ccode: parameter countaining 3 example country
            codes.

    Given: A Flask test client and expected parameter values for country
           name, year 2001, max arrivals, and country code.
    When: A HTTP GET request is made for a particular country row.
    Then: - The correct JSON response is returned
          - The correct the expected parameter values returned.
          - Response status code is 200 if country name is valid or 404
            if it is invalid.
    """
    expected_types, non_nullable_columns = expected_column_value_types

    # Query the Country_Name column using db.session.query()
    result = db.session.query(TourismArrivals.Country_Name).all()
    valid_country_names = [row[0] for row in result]

    # Send a GET request to retrieve data for a specific country
    response = test_client.get(
        f"/api/countries/country/{expected_result_cname}"
    )
    country_response_json = response.json

    # If country name is invalid, assert that a 404 error returned
    if expected_result_cname not in valid_country_names:
        expected_error_message = {
            "status": 404,
            "error": "Not found",
            "message": "Invalid resource URI: Invalid Country Name",
        }
        assert response.status_code == 404
        assert "Not found" in response.json["error"]
        assert country_response_json == expected_error_message
    # Else, if name is valid, check if all variables match expected
    else:
        # Create dictionary with column names as keys and the
        # parametrized expected variables as the values
        variables_dict = {
            "Country_Name": expected_result_cname,
            "year_2001": expected_result_year2001,
            "Max_number_of_arrivals": expected_result_max,
            "Country_Code": expected_result_ccode,
        }
        # Check if expected results match the actual results
        for column_name, expected_result in variables_dict.items():
            assert country_response_json[column_name] == expected_result
            assert response.status_code == 200


@pytest.mark.parametrize(
    "year",
    [
        # First set of valid years
        "1995",
        "2000",
        "2010",
        "2015",
        "2020",
        # Second set of invalid years
        "1900",
        "1000",
        "0",
        "3000",
        "text",
    ],
)
def test_filter_by_year_for_valid_and_invalid_years_combined(
    test_client, year, expected_lengths_row_count
):
    """
    Test if GET request is made for a particular year column.

    Tests if a HTTP GET request made for a particular year column
    returns all countries associated with that column and its values.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.
        year: parameter containing strings of 5 valid years and 5 invalid
            years entered in URI, to obtain results for.
        expected_lengths_row_count: fixture that dynamically checks row
            count of the current database, even if new entries posted.

    Given: A Flask test client and example parameter values for valid
           and invalid year columns.
    When: A HTTP GET request made to the URI for that year column.
    Then: - For invalid years a 404 status, error and correct error
            message is returned.
          - For valid years, a 200 status code and the correct JSON
            length, messages and
    """
    # If year is a number
    if year.isdigit():
        if int(year) < 1995 or int(year) > 2020:
            # Test case 2: Invalid years endpoint
            response = test_client.get(f"/api/filterby/year/{year}")
            # Assert correct error first raised
            assert AttributeError
            # Assert correct response code, JSON error messages returned
            expected_message = "Invalid resource URI: Invalid year"
            assert response.status_code == 404
            assert response.json["status"] == 404
            assert response.json["error"] == "Not found"
            assert response.json["message"] == expected_message
        # Test case 2: Valid years endpoints
        else:
            # Check if correct response code, correct JSON length
            response = test_client.get(f"/api/filterby/year/{year}")
            assert response.status_code == 200
            expected_length = (
                expected_lengths_row_count[year]
                if year in expected_lengths_row_count
                else 0
            )
            assert len(response.json) == expected_length

            # Check if correct keys in returned JSON
            if expected_length != 0:
                assert "Country_Name" in response.json[0]
                assert f"year_{year}" in response.json[0]
    # If year is a string/text instead of number
    else:
        # Assert error and correct custom messages upon GET request
        response = test_client.get(f"/api/filterby/year/{year}")
        assert HTTPError
        assert response.status_code == 404
        assert response.json["status"] == 404
        assert response.json["error"] == "Not found"
        assert response.json["message"] == "Invalid resource URI: Invalid year"


def test_top_10_countries_2020(
    test_client,
    new_top_country_for_top_10,
    top_10_countries_expected,
):
    """
    Test GET request for top 10 countries in average arrivals.

    Tests the HTTP GET request for top 10 countries in terms of average
    in the past 10 recorded years, if it returns the correct country,
    dynamically, even if a new one with a very high average is added.

    Args:
        test_client: fixture containing test client instance of app, to
            allow the tests to interact with the Flask server.
        new_top_country_for_top_10: fixture containing details of a new
            country with very high average to alter current top 10.
        top_10_countries_expected: fixture containing expected order of
            top 10 countries, their names and corresponding values.

    Given:- A Flask test client.
            - Details of a new country with very high average.
            - Expected order of top 10 countries, their names & values.
    When: - A GET request is made to the '/api/top-10-countries' endpoint
    Then: - The response status code should be 200 OK
        - The response should be valid JSON
        - The response should contain the correct top countries' keys
        - The response should contain the expected top 10 countries, and
          their values dynamically, even with a new country added
    """
    # Add a test country from fixture with very high average
    db.session.add(new_top_country_for_top_10)
    db.session.commit()

    # Assert correct status code upon GET request to endpoint
    response = test_client.get("/api/top-10-countries")
    assert response.status_code == 200

    # Check that the response is valid JSON
    data = json.loads(response.data)
    assert isinstance(data, dict)

    # Check that the response contains the correct top countries' keys
    assert "Top 10 countries for tourist arrivals" in data.keys()
    assert isinstance(data["Top 10 countries for tourist arrivals"], list)
    assert len(data["Top 10 countries for tourist arrivals"]) == 10

    # Check that the response contains the expected top 10 countries,
    # and their values dynamically, even with a new country added
    for country in data["Top 10 countries for tourist arrivals"]:
        assert country["Country_Name"] in top_10_countries_expected.keys()
