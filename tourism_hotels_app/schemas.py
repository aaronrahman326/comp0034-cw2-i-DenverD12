from tourism_hotels_app.models import TourismArrivals
from tourism_hotels_app import db, ma


# -------------------------
# Flask-Marshmallow Schemas
# See https://marshmallow-sqlalchemy.readthedocs.io/en/latest/#generate-marshmallow-schemas
# -------------------------


class TourismArrivalsSchema(ma.SQLAlchemySchema):
    """Marshmallow schema defining the attributes for creating a new country entry for tourist arrivals."""

    class Meta:
        # State the name of the model class
        model = TourismArrivals
        # Deserialize to model instances
        load_instance = True
        # Tell Marshmallow session to use to work with database
        sqla_session = db.session
        include_relationships = True
        # Order all json entries by order of entry
        ordered = True
        #! Remove below and above later if not using multiple tables
        #! include_fk = True

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
