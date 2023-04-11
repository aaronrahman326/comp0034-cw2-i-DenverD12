import pytest
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app.schemas import TourismArrivalsSchema
from tourism_hotels_app import db
import json

# Define Schemas
countries_schema = TourismArrivalsSchema(many=True)
country_schema = TourismArrivalsSchema()


def test_country_added_when_add_country(
        test_client, 
        country_example_base_valid_model,
        country_example_base_valid_json,
        country_example_valid_model_with_valid_nulls,
        country_example_valid_json_with_valid_nulls,
):
    test_case_list = {
        country_example_base_valid_model: country_example_base_valid_json,
        country_example_valid_model_with_valid_nulls:
        country_example_valid_json_with_valid_nulls,
    }

    for model, model_json in test_case_list.items():
        country_example_model = model
        country_example_json = model_json

    # Check if the country exists, if it does then delete it
    exists = db.session.execute(
        db.select(TourismArrivals).filter_by(Country_Name=country_example_model.Country_Name)
    ).scalar()
    if exists:
        # if region does exist, then delete it
        db.session.execute(db.delete(TourismArrivals).where(TourismArrivals.Country_Name == country_example_model.Country_Name))
        db.session.commit()

    # Count the number of regions before adding a new one
    num_countries_in_db = db.session.scalar(
        db.select(db.func.count()).select_from(TourismArrivals)
    )

    # Add a new region route
    response = test_client.post("/api/countries", json=country_example_json)
    # Count the number of regions after the new region is added
    num_countries_in_db_after = db.session.scalar(
        db.select(db.func.count()).select_from(TourismArrivals)
    )
    data = response.json

    for key, value in country_example_json.items():
        assert data[f"{key}"] == value

        
    assert response.status_code == 201
    assert num_countries_in_db_after == num_countries_in_db + 1