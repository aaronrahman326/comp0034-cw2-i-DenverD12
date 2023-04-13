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
    """Create a Flask test client for flask routes test."""
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client


# Define important fixture to dynamically track correct
# number of rows, even if a new one is posted
@pytest.fixture(scope="function")
def expected_lengths_row_count(test_client):
    """Return a dictionary of expected response lengths per year."""
    # Query database to get number of countries for each year
    years = ["1995", "2000", "2010", "2015", "2020"]
    expected_lengths = {}
    for year in years:
        response = test_client.get(f"/api/filterby/year/{year}")
        expected_lengths[year] = len(response.json)

    return expected_lengths


@pytest.fixture(scope="function")
def top_10_countries_expected(test_client):
    """Return dictionary with top 10 countries and average values."""
    # An expected dictionary of Top 10 countries and values,
    # after a new mock TestCountry added, Which changed top 10
    top_10_countries_expected_dict = {
        "TestCountry": "9999999999999",
        "France": "196572800",
        "United States": "158278026.6",
        "China": "130580500",
        "Spain": "104183800",
        "Mexico": "83798500",
        "Italy": "78958560.16",
        "Poland": "76742111.11",
        "Croatia": "50864700",
        "Hong Kong SAR, China": "50473900",
    }
    return top_10_countries_expected_dict


@pytest.fixture(scope="function")
def new_top_country_for_top_10(test_client):
    """Return an updated SQLAlchemy database model for one country."""
    # Define a new country row for tourism database
    # Include very high average to change top 10
    new_country_row = TourismArrivals(
        Country_Name="TestCountry",
        Region="TestRegion",
        IncomeGroup="TestIncomeGroup",
        Country_Code="TST",
        Indicator_Name="TestIndicator",
        Average_10year_in_tourist_arrivals="9999999999999",
    )
    return new_country_row


# Define a base fixture for an example valid country object 1 from model
@pytest.fixture(scope="module")
def country_example_base_valid_model():
    """Create a new tourism arrivals country object for tests."""
    country_example_model_1 = TourismArrivals(
        Country_Name="New Country",
        Region="New Region",
        IncomeGroup="High Income",
        Country_Code="TEST",
        Indicator_Name="International tourism, number of arrivals",
        year_1995=1,
        year_1996=1,
        year_1997=1,
        year_1998=1,
        year_1999=1,
        year_2000=1,
        year_2001=1,
        year_2002=1,
        year_2003=1,
        year_2004=1,
        year_2005=1,
        year_2006=1,
        year_2007=1,
        year_2008=1,
        year_2009=1,
        year_2010=1,
        year_2011=1,
        year_2012=1,
        year_2013=1,
        year_2014=1,
        year_2015=1,
        year_2016=1,
        year_2017=1,
        year_2018=1,
        year_2019=1,
        year_2020=1,
        Average_10year_in_tourist_arrivals="10.1",
        Max_number_of_arrivals=1,
        Minimum_number_of_arrivals=1,
        Percent_drop_2019_to_2020="10%",
    )
    return country_example_model_1


# Define a base fixture for an example valid country json 1
@pytest.fixture(scope="module")
def country_example_base_valid_json():
    """Create a new tourism arrivals country JSON for tests."""
    new_country_test_json_1 = {
        "Country_Name": "New Country",
        "Region": "New Region",
        "IncomeGroup": "High Income",
        "Country_Code": "TEST",
        "Indicator_Name": "International tourism, number of arrivals",
        "year_1995": 1,
        "year_1996": 1,
        "year_1997": 1,
        "year_1998": 1,
        "year_1999": 1,
        "year_2000": 1,
        "year_2001": 1,
        "year_2002": 1,
        "year_2003": 1,
        "year_2004": 1,
        "year_2005": 1,
        "year_2006": 1,
        "year_2007": 1,
        "year_2008": 1,
        "year_2009": 1,
        "year_2010": 1,
        "year_2011": 1,
        "year_2012": 1,
        "year_2013": 1,
        "year_2014": 1,
        "year_2015": 1,
        "year_2016": 1,
        "year_2017": 1,
        "year_2018": 1,
        "year_2019": 1,
        "year_2020": 1,
        "Average_10year_in_tourist_arrivals": "10.1",
        "Max_number_of_arrivals": 1,
        "Minimum_number_of_arrivals": 1,
        "Percent_drop_2019_to_2020": "10%",
    }
    return new_country_test_json_1


# Define a valid base country object 2 from model with valid nulls.
@pytest.fixture(scope="module")
def country_example_valid_model_with_valid_nulls(
    country_example_base_valid_model
):
    """Create a new tourism arrivals country object with valid nulls."""
    # Remove '_sa_instance_state' key from object's __dict__ to prevent
    # TypeError when creating a new object from updated dictionary.
    country_example_base_model_dict = {
        key: value
        for key, value in country_example_base_valid_model.__dict__.items()
        if key != "_sa_instance_state"
    }
    # Update and return created model object
    country_example_base_model_dict.update(
        {"year_2015": None, "Percent_drop_2019_to_2020": None}
    )
    return TourismArrivals(**country_example_base_model_dict)


# Define valid base country JSON 2 from model with valid nulls
@pytest.fixture(scope="module")
def country_example_valid_json_with_valid_nulls(
    country_example_base_valid_json
):
    """Create a new tourism arrivals country JSON with valid nulls."""
    country_example_base_valid_json["year_2015"] = None
    country_example_base_valid_json["Percent_drop_2019_to_2020"] = None
    return country_example_base_valid_json


# Define invalid base country object from model with invalid nulls
@pytest.fixture(scope="module")
def country_example_invalid_model_with_invalid_nulls(
    country_example_base_valid_model
):
    """Create a new tourism country object with invalid nulls."""
    # Remove '_sa_instance_state' key from object's __dict__ to prevent
    # TypeError when creating a new object from updated dictionary.
    country_example_base_model_dict = {
        key: value
        for key, value in country_example_base_valid_model.__dict__.items()
        if key != "_sa_instance_state"
    }
    # Set an invalid null value for IncomeGroup - does not allow nulls
    # Set a valid null just to show test will fail even if one invalid
    country_example_base_model_dict.update(
        {"IncomeGroup": None, "year_2003": None}
    )
    return TourismArrivals(**country_example_base_model_dict)


# Define invalid base country JSON with invalid nulls
@pytest.fixture(scope="module")
def country_example_invalid_json_with_invalid_nulls(
    country_example_base_valid_json
):
    """Create a new tourism country JSON with invalid nulls."""
    # Set an invalid null value for IncomeGroup - does not allow nulls
    country_example_base_valid_json["IncomeGroup"] = None
    # Set a valid null just to show test will fail even if one invalid
    country_example_base_valid_json["year_2003"] = None
    return country_example_base_valid_json


# Helper fixture used by many other fixtures
@pytest.fixture(scope="module")
def expected_column_value_types():
    """Return column names, expected tyoes and non-nullable columns."""
    # Define a dictionary with keys as column names and values
    # Values contain column expected data types
    expected_types = {
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

    non_nullable_columns = {
        "Country_Name": str,
        "Region": str,
        "IncomeGroup": str,
        "Country_Code": str,
        "Indicator_Name": str,
    }

    return expected_types, non_nullable_columns
