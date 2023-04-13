""""""
# ! Remove later: command for individual: pytest tests/test_api_obtain_data_routes.py/test_get_all_countries
import pytest
import json
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app import db
from flask import jsonify
from urllib.error import HTTPError

# Define Schemas
countries_schema = TourismArrivalsSchema(many=True)
country_schema = TourismArrivalsSchema()


def test_get_all_countries(test_client, expected_keys):
    # Make a GET request to the `/countries` endpoint
    response = test_client.get("/api/countries")

    assert response.status_code == 200

    # Deserialize the response content to a Python list
    response_data = json.loads(response.data)

    # Assert that the response is not empty
    assert len(response_data) > 0

    # Define expected keys from the created fixture
    expected_keys_dict = expected_keys

    # Assert that each item in the response has the expected keys
    for country_data in response_data:
        assert set(country_data.keys()) == expected_keys_dict


@pytest.mark.parametrize(
    (
        "expected_result_cname",
        "expected_result_year2001",
        "expected_result_max",
        "expected_result_ccode",
    ),
    (
        (
            "Aruba",
            1178000,
            1951000,
            "ABW",
        ),
        (
            "Zimbabwe",
            2217000,
            2580000,
            "ZWE",
        ),
        (
            "India",
            2537000,
            17914000,
            "IND",
        ),
        (
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
    GIVEN:
    WHEN:
    THEN:
    """
    expected_types, non_nullable_columns = expected_column_value_types

    # Query the Country_Name column using db.session.query()
    result = db.session.query(TourismArrivals.Country_Name).all()
    valid_country_names = [row[0] for row in result]

    # Print the list of country names
    print(f"This is a list of names: {valid_country_names}")

    response = test_client.get(f"/api/countries/country/{expected_result_cname}")
    country_response_json = response.json

    variables_dict = {
        "Country_Name": expected_result_cname,
        "year_2001": expected_result_year2001,
        "Max_number_of_arrivals": expected_result_max,
        "Country_Code": expected_result_ccode,
    }

    if expected_result_cname not in valid_country_names:
        expected_error_message = {
            "status": 404,
            "error": "Not found",
            "message": "Invalid resource URI: Invalid Country Name",
        }
        assert KeyError
        assert response.status_code == 404
        assert "Not found" in response.json["error"]
        assert country_response_json == expected_error_message
    else:
        for column_name, expected_result in variables_dict.items():
            assert country_response_json[column_name] == expected_result
            assert response.status_code == 200


@pytest.mark.parametrize(
    "year",
    ["1995", "2000", "2010", "2015", "2020", "1900", "1000", "0", "3000", "text"],
)
def test_filter_by_year_for_valid_and_invalid_years_combined(
    test_client, year, expected_lengths_row_count
):
    if year.isdigit():
        if int(year) < 1995 or int(year) > 2020:
            # Test case 3: Check if the endpoint returns the correct error message for an invalid year
            response = test_client.get(f"/api/filterby/year/{year}")
            assert response.status_code == 404
            assert response.json["status"] == 404
            assert response.json["error"] == "Not found"
            assert response.json["message"] == "Invalid resource URI: Invalid year"
            assert AttributeError
        else:
            # Test case 1: Check if the response is successful and the returned JSON has the correct length
            response = test_client.get(f"/api/filterby/year/{year}")
            assert response.status_code == 200
            expected_length = (
                expected_lengths_row_count[year]
                if year in expected_lengths_row_count
                else 0
            )
            assert len(response.json) == expected_length

            # Test case 2: Check if the returned JSON contains the correct keys
            if expected_length != 0:
                assert "Country_Name" in response.json[0]
                assert f"year_{year}" in response.json[0]
    else:
        response = test_client.get(f"/api/filterby/year/{year}")
        assert HTTPError
        assert response.status_code == 404
        assert response.json["status"] == 404
        assert response.json["error"] == "Not found"
        assert response.json["message"] == "Invalid resource URI: Invalid year"


def test_top_10_countries_2020(test_client, top_10_countries_expected):
    # Add a new row to test if top 10 is updated
    new_country = TourismArrivals(
        Country_Name="TestCountry",
        Region="TestRegion",
        IncomeGroup="TestIncomeGroup",
        Country_Code="TST",
        Indicator_Name="TestIndicator",
        Average_10year_in_tourist_arrivals="9999999999999",
    )
    db.session.add(new_country)
    db.session.commit()

    response = test_client.get("/api/top-10-countries")
    assert response.status_code == 200

    # Check that the response is valid JSON
    data = json.loads(response.data)
    assert isinstance(data, dict)

    # Check that the response contains the correct keys
    assert "Top 10 countries for tourist arrivals" in data.keys()
    assert isinstance(data["Top 10 countries for tourist arrivals"], list)
    assert len(data["Top 10 countries for tourist arrivals"]) == 10

    # Check that the response contains the expected top 10 countries,
    # and their values dynamically, even with a new country added

    for country in data["Top 10 countries for tourist arrivals"]:
        assert country["Country_Name"] in top_10_countries_expected.keys()
