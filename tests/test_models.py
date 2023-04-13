"""File that tests the SQLAlchemy database model instances."""


def test_create_new_country(country_example_base_valid_model):
    """
    Tests if the SQLAlchemy model is made correctly.

    Args:
        country_example_base_valid_model: fixture containing a base
        country model with all correct features and all columns.

    GIVEN: A fixture with Json data for a country.
    WHEN: A new country object is created.
    THEN: Check the fields are defined correctly and match given data.
    """

    # Assert correct fields are defined in model
    assert country_example_base_valid_model.Country_Name == "New Country"
    assert country_example_base_valid_model.Region == "New Region"
    assert country_example_base_valid_model.IncomeGroup == "High Income"
    assert country_example_base_valid_model.Country_Code == "TEST"
    assert country_example_base_valid_model.Indicator_Name == \
        "International tourism, number of arrivals"
    assert country_example_base_valid_model.year_1995 == 1
    assert country_example_base_valid_model.year_1996 == 1
    assert country_example_base_valid_model.year_1995 == 1
    assert country_example_base_valid_model.year_1996 == 1
    assert country_example_base_valid_model.year_1997 == 1
    assert country_example_base_valid_model.year_1998 == 1
    assert country_example_base_valid_model.year_1999 == 1
    assert country_example_base_valid_model.year_2000 == 1
    assert country_example_base_valid_model.year_2001 == 1
    assert country_example_base_valid_model.year_2002 == 1
    assert country_example_base_valid_model.year_2003 == 1
    assert country_example_base_valid_model.year_2004 == 1
    assert country_example_base_valid_model.year_2005 == 1
    assert country_example_base_valid_model.year_2006 == 1
    assert country_example_base_valid_model.year_2007 == 1
    assert country_example_base_valid_model.year_2008 == 1
    assert country_example_base_valid_model.year_2009 == 1
    assert country_example_base_valid_model.year_2010 == 1
    assert country_example_base_valid_model.year_2011 == 1
    assert country_example_base_valid_model.year_2012 == 1
    assert country_example_base_valid_model.year_2013 == 1
    assert country_example_base_valid_model.year_2014 == 1
    assert country_example_base_valid_model.year_2015 == 1
    assert country_example_base_valid_model.year_2016 == 1
    assert country_example_base_valid_model.year_2017 == 1
    assert country_example_base_valid_model.year_2018 == 1
    assert country_example_base_valid_model.year_2019 == 1
    assert country_example_base_valid_model.year_2020 == 1
    assert country_example_base_valid_model.\
        Average_10year_in_tourist_arrivals == "10.1"
    assert country_example_base_valid_model.Max_number_of_arrivals == 1
    assert country_example_base_valid_model.Minimum_number_of_arrivals == 1
    assert country_example_base_valid_model.Percent_drop_2019_to_2020 == "10%"
