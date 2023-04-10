from tourism_hotels_app.models import TourismArrivals


def test_create_new_country():
    """
    GIVEN json data for a country
    WHEN a new country object is created
    THEN check the fields are defined correctly
    """
    test_model = TourismArrivals(
        Country_Name="New Country", Region="New Region",
        IncomeGroup="High Income", Country_Code="TEST",
        Indicator_Name="International tourism, number of arrivals",
        year_1995=1, year_1996=1, year_1997=1, year_1998=1, year_1999=1,
        year_2000=1, year_2001=1, year_2002=1, year_2003=1, year_2004=1,
        year_2005=1, year_2006=1, year_2007=1, year_2008=1, year_2009=1,
        year_2010=1, year_2011=1, year_2012=1, year_2013=1, year_2014=1,
        year_2015=1, year_2016=1, year_2017=1, year_2018=1, year_2019=1,
        year_2020=1, Average_10year_in_tourist_arrivals="10.1",
        Max_number_of_arrivals=1, Minimum_number_of_arrivals=2,
        Percent_drop_2019_to_2020="10%",
    )

    assert test_model.Country_Name == "New Country"
    assert test_model.Region == "New Region"
    assert test_model.IncomeGroup == "High Income"
    assert test_model.Country_Code == "TEST"
    assert test_model.Indicator_Name == "International tourism, number of arrivals"
    assert test_model.year_1995 == 1
    assert test_model.year_1996 == 1
    assert test_model.year_1995 == 1
    assert test_model.year_1996 == 1
    assert test_model.year_1997 == 1
    assert test_model.year_1998 == 1
    assert test_model.year_1999 == 1
    assert test_model.year_2000 == 1
    assert test_model.year_2001 == 1
    assert test_model.year_2002 == 1
    assert test_model.year_2003 == 1
    assert test_model.year_2004 == 1
    assert test_model.year_2005 == 1
    assert test_model.year_2006 == 1
    assert test_model.year_2007 == 1
    assert test_model.year_2008 == 1
    assert test_model.year_2009 == 1
    assert test_model.year_2010 == 1
    assert test_model.year_2011 == 1
    assert test_model.year_2012 == 1
    assert test_model.year_2013 == 1
    assert test_model.year_2014 == 1
    assert test_model.year_2015 == 1
    assert test_model.year_2016 == 1
    assert test_model.year_2017 == 1
    assert test_model.year_2018 == 1
    assert test_model.year_2019 == 1
    assert test_model.year_2020 == 1
    assert test_model.Average_10year_in_tourist_arrivals == "10.1"
    assert test_model.Max_number_of_arrivals == 1
    assert test_model.Minimum_number_of_arrivals == 2
    assert test_model.Percent_drop_2019_to_2020 == "10%"


# def test_create_new_country():
#     """
#     GIVEN json data for a country
#     WHEN a new country object is created
#     THEN check the fields are defined correctly
#     """
#     test_model = TourismArrivals(
#         Country_Name="New Country", Region="New Region",
#         IncomeGroup="High Income", Country_Code="TEST",
#         Indicator_Name="International tourism, number of arrivals",
#         year_1995=1, year_1996=1, year_1997=1, year_1998=1, year_1999=1,
#         year_2000=1, year_2001=1, year_2002=1, year_2003=1, year_2004=1,
#         year_2005=1, year_2006=1, year_2007=1, year_2008=1, year_2009=1,
#         year_2010=1, year_2011=1, year_2012=1, year_2013=1, year_2014=1,
#         year_2015=1, year_2016=1, year_2017=1, year_2018=1, year_2019=1,
#         year_2020=1, Average_10year_in_tourist_arrivals="10.1",
#         Max_number_of_arrivals=1, Minimum_number_of_arrivals=2,
#         Percent_drop_2019_to_2020="10%",
#     )
#     try:
#         assert test_model.Country_Name == "New Country"
#         assert test_model.Region == "New Region"
#         assert test_model.IncomeGroup == "High Income"
#         assert test_model.Country_Code == "TEST"
#         assert test_model.Indicator_Name == "International tourism, number of arrivals"
#         assert test_model.year_1995 == 1
#         assert test_model.year_1996 == 1
#         assert test_model.year_1995 == 1
#         assert test_model.year_1996 == 1
#         assert test_model.year_1997 == 1
#         assert test_model.year_1998 == 1
#         assert test_model.year_1999 == 1
#         assert test_model.year_2000 == 1
#         assert test_model.year_2001 == 1
#         assert test_model.year_2002 == 1
#         assert test_model.year_2003 == 1
#         assert test_model.year_2004 == 1
#         assert test_model.year_2005 == 1
#         assert test_model.year_2006 == 1
#         assert test_model.year_2007 == 1
#         assert test_model.year_2008 == 1
#         assert test_model.year_2009 == 1
#         assert test_model.year_2010 == 1
#         assert test_model.year_2011 == 1
#         assert test_model.year_2012 == 1
#         assert test_model.year_2013 == 1
#         assert test_model.year_2014 == 1
#         assert test_model.year_2015 == 1
#         assert test_model.year_2016 == 1
#         assert test_model.year_2017 == 1
#         assert test_model.year_2018 == 1
#         assert test_model.year_2019 == 1
#         assert test_model.year_2020 == 1
#         assert test_model.Average_10year_in_tourist_arrivals == "10.1"
#         assert test_model.Max_number_of_arrivals == 1
#         assert test_model.Minimum_number_of_arrivals == 2
#         assert test_model.Percent_drop_2019_to_2020 == "10%"
#     except ValueError:
#         assert
