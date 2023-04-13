"""File containing SQLAlchemy Schema's created from the database model."""
from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app import db, ma


# -------------------------
# Flask-Marshmallow Schemas
# -------------------------
class TourismArrivalsSchema(ma.SQLAlchemySchema):
    """
    Marshmallow schema defining attributes for creating a new country.

    This class defines a Marshmallow schema that is used to serialize
    and deserialize data from the TourismArrivals model to JSON, and
    vice versa.

    Attributes:
    -----------
    Meta: Subclass of SQLAlchemy's MetaData that holds the name of the
        model class, deserialization flag and session object to
        use when working, with database.
    Country_Name : Auto-generated field, corresponds to the Country_Name
        column in TourismArrivals table.
    Region : Auto-generated field that corresponds to Region column in
        TourismArrivals table.
    IncomeGroup : Auto-generated field that corresponds to IncomeGroup
        column in TourismArrivals table.
    Country_Code : Auto-generated field that corresponds to Country_Code
        column in TourismArrivals table.
    Indicator_Name : Auto-generated field that corresponds to
        Indicator_Name column in TourismArrivals table.
    year_1995 - year_2020 : Auto-generated fields that correspond to
        yearly columns in TourismArrivals table.
    Average_10year_in_tourist_arrivals : Auto-generated field that
        corresponds to Average_10year_in_tourist_arrivals column in
        TourismArrivals table.
    Max_number_of_arrivals : Auto-generated field that corresponds to
        Max_number_of_arrivals column in TourismArrivals table.
    Minimum_number_of_arrivals : Auto-generated field that corresponds
        to Minimum_number_of_arrivals column in TourismArrivals table.
    Percent_drop_2019_to_2020 : Auto-generated field that corresponds
        to Percent_drop_2019_to_2020 column in TourismArrivals table.
    """

    class Meta:
        """Subclass of SQLAlchemy's MetaData."""

        # State the name of the model class
        model = TourismArrivals
        # Deserialize to model instances
        load_instance = True
        # Tell Marshmallow session to use to work with database
        sqla_session = db.session
        include_relationships = True
        # Order all json entries by order of entry to prevent random
        ordered = True

    # Specify the fields to include in the schema
    Country_Name = ma.auto_field()
    Region = ma.auto_field()
    IncomeGroup = ma.auto_field()
    Country_Code = ma.auto_field()
    Indicator_Name = ma.auto_field()
    year_1995 = ma.auto_field()
    year_1996 = ma.auto_field()
    year_1997 = ma.auto_field()
    year_1998 = ma.auto_field()
    year_1999 = ma.auto_field()
    year_2000 = ma.auto_field()
    year_2001 = ma.auto_field()
    year_2002 = ma.auto_field()
    year_2003 = ma.auto_field()
    year_2004 = ma.auto_field()
    year_2005 = ma.auto_field()
    year_2006 = ma.auto_field()
    year_2007 = ma.auto_field()
    year_2008 = ma.auto_field()
    year_2009 = ma.auto_field()
    year_2010 = ma.auto_field()
    year_2011 = ma.auto_field()
    year_2012 = ma.auto_field()
    year_2013 = ma.auto_field()
    year_2014 = ma.auto_field()
    year_2015 = ma.auto_field()
    year_2016 = ma.auto_field()
    year_2017 = ma.auto_field()
    year_2018 = ma.auto_field()
    year_2019 = ma.auto_field()
    year_2020 = ma.auto_field()
    Average_10year_in_tourist_arrivals = ma.auto_field()
    Max_number_of_arrivals = ma.auto_field()
    Minimum_number_of_arrivals = ma.auto_field()
    Percent_drop_2019_to_2020 = ma.auto_field()
