import pytest
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app import db
import json

# -------
# Schemas
# -----
regions_schema = TourismArrivalsSchema(many=True)
region_schema = TourismArrivalsSchema()


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
    ),
)
def test_when_get_specific_country_then_correct_json_returned(
    test_client,
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
    response = test_client.get(
        f"/api/countries/filterby/country/{expected_result_cname}"
    )

    assert response.status_code == 200

    country_json = response.json

    variables_dict = {
        "Country_Name": expected_result_cname,
        "year_2001": expected_result_year2001,
        "Max_number_of_arrivals": expected_result_max,
        "Country_Code": expected_result_ccode,
    }

    for key, value in variables_dict.items():
        assert country_json[key] == value


@pytest.mark.parametrize("year", ["1995", "2000", "2010", "2015", "2020"])
def test_by_year_parametrized(test_client, year):
    # Test case 1: Check if the response is successful and the returned JSON has the correct length
    response = test_client.get(f'/api/filterby/year/{year}')
    assert response.status_code == 200
    assert len(response.json) == 195

    # Test case 2: Check if the returned JSON contains the correct keys
    response = test_client.get(f'/api/filterby/year/{year}')
    assert response.status_code == 200
    assert 'Country_Name' in response.json[0]
    assert f'year_{year}' in response.json[0]


@pytest.mark.parametrize("year", ["1900", "1000", "0", "3000", "text"])
def test_by_year_invalid_year(test_client, year):

    # Test case 3: Check if the endpoint returns the correct error message for an invalid year
    response = test_client.get(f'/api/filterby/year/{year}')
    assert response.status_code == 404
    assert response.json['status'] == 404
    assert response.json['error'] == 'Not found'
    assert response.json['message'] == 'Invalid resource URI: Invalid year'


@pytest.mark.parametrize("year", ["1995", "2000", "2010", "2015", "2020", "1900", "1000", "0", "3000", "text"])
def test_filter_by_year(test_client, year, expected_lengths_row_count):
    if year.isdigit():
        if int(year) < 1995 or int(year) > 2020:
            # Test case 3: Check if the endpoint returns the correct error message for an invalid year
            response = test_client.get(f'/api/filterby/year/{year}')
            assert response.status_code == 404
            assert response.json['status'] == 404
            assert response.json['error'] == 'Not found'
            assert response.json['message'] == 'Invalid resource URI: Invalid year'
        else:
            # Test case 1: Check if the response is successful and the returned JSON has the correct length
            response = test_client.get(f'/api/filterby/year/{year}')
            assert response.status_code == 200
            expected_length = expected_lengths_row_count[year] if year in expected_lengths_row_count else 0
            assert len(response.json) == expected_length

            # Test case 2: Check if the returned JSON contains the correct keys
            if expected_length != 0:
                assert 'Country_Name' in response.json[0]
                assert f'year_{year}' in response.json[0]
    else:
        response = test_client.get(f'/api/filterby/year/{year}')
        assert response.status_code == 404
        assert response.json['status'] == 404
        assert response.json['error'] == 'Not found'
        assert response.json['message'] == 'Invalid resource URI: Invalid year'
