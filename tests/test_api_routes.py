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


@pytest.mark.parametrize(
    (
        "country_name",
        "expected_result_cname",
        "year_2001",
        "expected_result_year2001",
        "Max_number_of_arrivals",
        "expected_result_max",
    ),
    (
        (
            "Aruba",
            "Aruba",
            "year_2001",
            1178000,
            "Max_number_of_arrivals",
            1951000,
        ),
        (
            "Zimbabwe",
            "Zimbabwe",
            "year_2001",
            2217000,
            "Max_number_of_arrivals",
            2580000,
        ),
    ),
)
def test_when_get_specific_country_then_correct_json_returned(
    test_client,
    country_name,
    expected_result_cname,
    year_2001,
    expected_result_year2001,
    Max_number_of_arrivals,
    expected_result_max,
):
    """
    GIVEN a running Flask app
    WHEN the "/noc/<code>" route is requested with the GBR code
    THEN the response should contain the region UK
    """
    response = test_client.get(f"/api/countries/filterby/country/{country_name}")
    assert response.status_code == 200

    assert isinstance(my_string, str)

    country_json = response.json
    assert country_json["Country_Name"] == f"{expected_result_cname}"
    assert country_json["year_2001"] == expected_result_year2001
    assert country_json["Max_number_of_arrivals"] == expected_result_max


def test_get_all_countries(test_client):
    # Make a GET request to the `/countries` endpoint
    response = test_client.get("/api/countries")
    assert response.status_code == 200

    # Deserialize the response content to a Python list
    response_data = json.loads(response.data)

    # Assert that the response is not empty
    assert len(response_data) > 0

    # Assert that each item in the response has the expected keys
    expected_keys = {
        "Country_Name",
        "Region",
        "IncomeGroup",
        "Country_Code",
        "Indicator_Name",
        "year_1995",
        "year_1996",
        "year_1997",
        "year_1998",
        "year_1999",
        "year_2000",
        "year_2001",
        "year_2002",
        "year_2003",
        "year_2004",
        "year_2005",
        "year_2006",
        "year_2007",
        "year_2008",
        "year_2009",
        "year_2010",
        "year_2011",
        "year_2012",
        "year_2013",
        "year_2014",
        "year_2015",
        "year_2016",
        "year_2017",
        "year_2018",
        "year_2019",
        "year_2020",
        "Average_10year_in_tourist_arrivals",
        "Max_number_of_arrivals",
        "Minimum_number_of_arrivals",
        "Percent_drop_2019_to_2020",
    }
    for country_data in response_data:
        assert set(country_data.keys()) == expected_keys