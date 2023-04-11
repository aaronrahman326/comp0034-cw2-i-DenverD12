"""All fixtures used in testing."""
import pytest
from tourism_hotels_app import create_app, config
from tourism_hotels_app.models import TourismArrivals


# Define an app instance fixture for flask routes test
@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing."""
    app = create_app(config.TestConfig)
    yield app


# Define a test client fixture for flask routes test
@pytest.fixture(scope="function")
def test_client(app):
    """Create a Flask test client."""
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client


# Define a fixture containing expected keys for all countries
@pytest.fixture(scope="function")
def expected_keys():
    expected_keys_dict = {
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
    yield expected_keys_dict


# Define important fixture to track correct number of rows,
# even if a new one is posted
@pytest.fixture(scope='function')
def expected_lengths_row_count(test_client):
    # Query the database to get the number of countries for each year
    years = ["1995", "2000", "2010", "2015", "2020"]
    expected_lengths = {}
    for year in years:
        response = test_client.get(f'/api/filterby/year/{year}')
        expected_lengths[year] = len(response.json)

    return expected_lengths


# Define a base fixture for an example valid country object 1 from model
@pytest.fixture(scope="module")
def country_example_base_valid_model():
    """Create a new tourism arrivals country object for tests."""
    country_example_model_1 = TourismArrivals(
        Country_Name="New Country", Region="New Region",
        IncomeGroup="High Income", Country_Code="TEST",
        Indicator_Name="International tourism, number of arrivals",
        year_1995=1, year_1996=1, year_1997=1, year_1998=1, year_1999=1,
        year_2000=1, year_2001=1, year_2002=1, year_2003=1, year_2004=1,
        year_2005=1, year_2006=1, year_2007=1, year_2008=1, year_2009=1,
        year_2010=1, year_2011=1, year_2012=1, year_2013=1, year_2014=1,
        year_2015=1, year_2016=1, year_2017=1, year_2018=1, year_2019=1,
        year_2020=1, Average_10year_in_tourist_arrivals="10.1",
        Max_number_of_arrivals=1, Minimum_number_of_arrivals=1,
        Percent_drop_2019_to_2020="10%",
    )
    return country_example_model_1


# Define a base fixture for an example valid country json 1
@pytest.fixture(scope="module")
def country_example_base_valid_json():
    """Create a new tourism arrivals country JSON for tests."""
    new_country_test_json_1 = {
        "Country_Name": "New Country", "Region": "New Region",
        "IncomeGroup": "High Income", "Country_Code": "TEST",
        "Indicator_Name": "International tourism, number of arrivals",
        "year_1995": 1, "year_1996": 1, "year_1997": 1, "year_1998": 1,
        "year_1999": 1, "year_2000": 1, "year_2001": 1, "year_2002": 1,
        "year_2003": 1, "year_2004": 1, "year_2005": 1, "year_2006": 1,
        "year_2007": 1, "year_2008": 1, "year_2009": 1, "year_2010": 1,
        "year_2011": 1, "year_2012": 1, "year_2013": 1, "year_2014": 1,
        "year_2015": 1, "year_2016": 1, "year_2017": 1, "year_2018": 1,
        "year_2019": 1, "year_2020": 1,
        "Average_10year_in_tourist_arrivals": "10.1",
        "Max_number_of_arrivals": 1, "Minimum_number_of_arrivals": 1,
        "Percent_drop_2019_to_2020": "10%",
    }
    return new_country_test_json_1


@pytest.fixture(scope="module")
def country_example_valid_json_with_valid_nulls(country_example_base_valid_json):
    country_example_base_valid_json["year_2015"] = None
    country_example_base_valid_json["Percent_drop_2019_to_2020"] = None
    return country_example_base_valid_json


@pytest.fixture(scope="module")
def country_example_valid_model_with_valid_nulls(country_example_base_valid_model):
    """Create a new tourism arrivals country object for tests."""
    # Remove '_sa_instance_state' key from object's __dict__ to prevent
    # TypeError when creating a new object from updated dictionary.
    country_example_base_model_dict = {
        k: v for k, v in country_example_base_valid_model.__dict__.items()
        if k != '_sa_instance_state'
    }
    country_example_base_model_dict.update({
        'year_2015': None,
        "Percent_drop_2019_to_2020": None
    })
    return TourismArrivals(**country_example_base_model_dict)


