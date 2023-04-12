import pytest
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app import db
import json
from sqlalchemy.exc import IntegrityError

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
    # Define valid test cases
    test_case_dictionary = {
        country_example_base_valid_model: country_example_base_valid_json,
        country_example_valid_model_with_valid_nulls:
        country_example_valid_json_with_valid_nulls,
    }

    for model, model_json in test_case_dictionary.items():
        country_example_model = model
        country_example_json = model_json

    # Check if the country exists, if it does then delete it
    exists = db.session.execute(
        db.select(TourismArrivals).filter_by(Country_Name=country_example_model.Country_Name)
    ).scalar()
    if exists:
        # if country does exist, then delete it
        db.session.execute(db.delete(TourismArrivals).where(TourismArrivals.Country_Name == country_example_model.Country_Name))
        db.session.commit()

    # Count the number of countries before adding a new one
    num_countries_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(TourismArrivals)
    )

    # Add a new country row via post route method
    response = test_client.post("/api/countries", json=country_example_json)
    # Count the number of countries after the new country is added
    num_countries_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(TourismArrivals)
    )
    data = response.json

    for key, value in country_example_json.items():
        assert data[f"{key}"] == value

    assert response.status_code == 201
    assert num_countries_in_db_after == num_countries_in_db + 1


def test_post_country_not_added_when_invalid_entry(
        test_client,
        expected_column_value_types,
        country_example_invalid_model_with_invalid_nulls,
        country_example_invalid_json_with_invalid_nulls
):
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
        db.select(TourismArrivals).filter_by(Country_Name=country_example_model.Country_Name)
    ).scalar()
    if exists:
        # if country does exist, then delete it
        db.session.execute(db.delete(TourismArrivals).where(TourismArrivals.Country_Name == country_example_model.Country_Name))
        db.session.commit()
        
    expected_types, non_nullable_columns = expected_column_value_types

    # Add a new country row via post route method
    response = test_client.post("/api/countries", json=country_example_json)
    assert response.status_code == 400

    # For the first 5 columns only, the entered data cannot be null
    for key in list(country_example_invalid_json_with_invalid_nulls.keys())[:5]:
        if key in non_nullable_columns:
            if not country_example_invalid_json_with_invalid_nulls[key]:
                assert ValueError(f"The value entered for IncomeGroup cannot be empty or null")


@pytest.mark.parametrize("country_name, example_valid_field_entries", [
    ("India", {"year_1995": 1000, "year_1996": 1500}),
    ("TestCountry", {"Region": "UpdatedRegion", "IncomeGroup": "UpdatedIncomeGroup"})
])
def test_edit_existing_country_with_valid_input(
    test_client, country_name, example_valid_field_entries
):
    """This function tests for two parametrized tests.
    One if for a Country Name that already exists in the database,
    And another for a custom (mock) country name that is first added
    to the database."""
    # If the test is for custom TestCountry,
    # Create the necessary data in the database
    if country_name == "TestCountry":
        existing_country = TourismArrivals(Country_Name=country_name, Region="TestRegion", IncomeGroup="TestIncomeGroup", Country_Code="TestCountryCode", Indicator_Name="TestIndicatorName", year_1995=100, year_1996=200, year_1997=300)
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
    updated_country = db.session.query(TourismArrivals).filter_by(Country_Name=country_name).first()
    # Check if all the fields in the request are updated in the database
    for key, value in data.items():
        assert getattr(updated_country, key) == value

    # Assertions specific to India test case
    if country_name == "India":
        assert 'Country_Name' in updated_country.__dict__.keys()
        assert updated_country.Country_Name == 'India'
        assert 'year_1995' in updated_country.__dict__.keys()
        assert updated_country.year_1995 == 1000
        assert 'year_1996' in updated_country.__dict__.keys()
        assert updated_country.year_1996 == 1500

    # Assertions specific to TestCountry test case
    if country_name == "TestCountry":
        # Check if the Region and IncomeGroup fields are updated in the database
        assert updated_country.Region == data["Region"]
        assert updated_country.IncomeGroup == data["IncomeGroup"]


def test_edit_existing_country_with_invalid_country_name(test_client):
    # Test data
    invalid_country_name_uri = 'Invalid Country'
    example_valid_entries = {
        "year_1995": 1000,
        "year_1996": 1500
    }

    # Make a request to the API
    response = test_client.patch(
        f'/api/countries/{invalid_country_name_uri}',
        json=example_valid_entries
    )
    data = response.get_json()

    # Assertions
    assert response.status_code == 404
    assert data['status'] == 404
    assert 'Not found' in data['error']


def test_edit_nonexistent_country(test_client):
    country_name = "NonexistentCountry"
    data = {"Region": "TestRegion", "IncomeGroup": "TestIncomeGroup"}

    response = test_client.patch(f"/api/countries/{country_name}", json=data)
    assert response.status_code == 404

    response_json = response.get_json()
    assert response_json["error"] == "Not found"
    assert response_json["message"] == "Invalid resource URI - That country does not exist"


def test_edit_existing_country_with_invalid_json_entry(test_client):
    # Test data
    country_name = 'India'
    example_invalid_entries = {
        "year_1995": "invalid string entry which should be integer"
    }

    # Make a request to the API
    response = test_client.patch(
        f'/api/countries/{country_name}', json=example_invalid_entries
    )

    # Assertions
    assert response.status_code == 400
    assert ValueError('The value entered for year_1995 should be of type: int')


def test_edit_existing_country_with_empty_payload(test_client):
    # Test data
    country_name = 'India'
    payload = {
        "Region": ""
    }

    # Make a request to the API
    response = test_client.patch(f'/api/countries/{country_name}', json=payload)

    # Assertions
    assert response.status_code == 400
    assert ValueError('The value entered for Region cannot be empty or null')
