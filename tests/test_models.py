

def test_create_new_country(country_example_model):
    """
    GIVEN json data for a country
    WHEN a new country object is created
    THEN check the fields are defined correctly
    """

    assert country_example_model.Country_Name == "New Country"
    assert country_example_model.Region == "New Region"
    assert country_example_model.IncomeGroup == "High Income"
    assert country_example_model.Country_Code == "TEST"
    assert country_example_model.Indicator_Name == \
        "International tourism, number of arrivals"
    assert country_example_model.year_1995 == 1
    assert country_example_model.year_1996 == 1
    assert country_example_model.year_1995 == 1
    assert country_example_model.year_1996 == 1
    assert country_example_model.year_1997 == 1
    assert country_example_model.year_1998 == 1
    assert country_example_model.year_1999 == 1
    assert country_example_model.year_2000 == 1
    assert country_example_model.year_2001 == 1
    assert country_example_model.year_2002 == 1
    assert country_example_model.year_2003 == 1
    assert country_example_model.year_2004 == 1
    assert country_example_model.year_2005 == 1
    assert country_example_model.year_2006 == 1
    assert country_example_model.year_2007 == 1
    assert country_example_model.year_2008 == 1
    assert country_example_model.year_2009 == 1
    assert country_example_model.year_2010 == 1
    assert country_example_model.year_2011 == 1
    assert country_example_model.year_2012 == 1
    assert country_example_model.year_2013 == 1
    assert country_example_model.year_2014 == 1
    assert country_example_model.year_2015 == 1
    assert country_example_model.year_2016 == 1
    assert country_example_model.year_2017 == 1
    assert country_example_model.year_2018 == 1
    assert country_example_model.year_2019 == 1
    assert country_example_model.year_2020 == 1
    assert country_example_model.Average_10year_in_tourist_arrivals == "10.1"
    assert country_example_model.Max_number_of_arrivals == 1
    assert country_example_model.Minimum_number_of_arrivals == 2
    assert country_example_model.Percent_drop_2019_to_2020 == "10%"
