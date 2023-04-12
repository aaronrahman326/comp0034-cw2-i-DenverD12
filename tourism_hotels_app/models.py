"""
This file is to define model classes.

These will map from the database to Python classes.
"""
from tourism_hotels_app import db


class TourismArrivals(db.Model):
    """
    Contains the SQLAlchemy model class.

    This defines a mapping between the `tourism_arrivals` table
    in the database and the corresponding Python class.

    Args:
        db.Model: Connects to SQLAlchemy database model function.

    Attributes:
        Country_Name (str): The name of the country (primary key).
        Region (str): The region where the country is located.
        IncomeGroup (str): The income group of the country.
        Country_Code (str): The code that identifies the country.
        Indicator_Name (str): The name of the tourism indicator.
        year_1995-2020 (int): The number of tourist arrivals in the
            respective year.
        Average_10year_in_tourist_arrivals (str): The 10-year average of
            tourist arrivals for each country.
        Max_number_of_arrivals (int): The all time maximum number of
            tourist arrivals.
        Minimum_number_of_arrivals (int): The all time minimum number of
            tourist arrivals for each country.
        Percent_drop_2019_to_2020 (str): The percentage of drop in tourist
            arrivals between 2019 and 2020.

    Methods:
        __repr__(): Returns the attributes of the country as a string.
        to_dict(): Returns a dictionary representation of the object.

    """

    __tablename__ = "tourism_arrivals"
    # Columns for each attribute, with descriptions and constraints
    # Set nulls to false for first 5 columns as every country must have
    Country_Name = db.Column(
        "Country Name", db.Text, unique=True, nullable=False, primary_key=True
    )
    Region = db.Column(db.Text, nullable=False)
    IncomeGroup = db.Column(db.Text, nullable=False)
    Country_Code = db.Column("Country Code", db.Text, nullable=False)
    Indicator_Name = db.Column("Indicator Name", db.Text, nullable=False)
    # Years may not have existing records so can be allowed nulls.
    year_1995 = db.Column("1995", db.Integer, nullable=True)
    year_1996 = db.Column("1996", db.Integer, nullable=True)
    year_1997 = db.Column("1997", db.Integer, nullable=True)
    year_1998 = db.Column("1998", db.Integer, nullable=True)
    year_1999 = db.Column("1999", db.Integer, nullable=True)
    year_2000 = db.Column("2000", db.Integer, nullable=True)
    year_2001 = db.Column("2001", db.Integer, nullable=True)
    year_2002 = db.Column("2002", db.Integer, nullable=True)
    year_2003 = db.Column("2003", db.Integer, nullable=True)
    year_2004 = db.Column("2004", db.Integer, nullable=True)
    year_2005 = db.Column("2005", db.Integer, nullable=True)
    year_2006 = db.Column("2006", db.Integer, nullable=True)
    year_2007 = db.Column("2007", db.Integer, nullable=True)
    year_2008 = db.Column("2008", db.Integer, nullable=True)
    year_2009 = db.Column("2009", db.Integer, nullable=True)
    year_2010 = db.Column("2010", db.Integer, nullable=True)
    year_2011 = db.Column("2011", db.Integer, nullable=True)
    year_2012 = db.Column("2012", db.Integer, nullable=True)
    year_2013 = db.Column("2013", db.Integer, nullable=True)
    year_2014 = db.Column("2014", db.Integer, nullable=True)
    year_2015 = db.Column("2015", db.Integer, nullable=True)
    year_2016 = db.Column("2016", db.Integer, nullable=True)
    year_2017 = db.Column("2017", db.Integer, nullable=True)
    year_2018 = db.Column("2018", db.Integer, nullable=True)
    year_2019 = db.Column("2019", db.Integer, nullable=True)
    year_2020 = db.Column("2020", db.Integer, nullable=True)
    Average_10year_in_tourist_arrivals = db.Column(
        "10-year Average in tourist arrivals", db.Text, nullable=True
    )
    Max_number_of_arrivals = db.Column(
        "Max number of arrivals", db.Integer, nullable=True
    )
    Minimum_number_of_arrivals = db.Column(
        "Minimum number of arrivals", db.Integer, nullable=True
    )
    Percent_drop_2019_to_2020 = db.Column(
        "Percent drop 2019 to 2020", db.Text, nullable=True
    )

    def __repr__(self):
        """
        Return the attributes of the country as a string.

        Args:
            self.
        Returns:
            Attributes/Column Names of the country as a string.
        """
        clsname = self.__class__.__name__
        return f"<\
            {clsname}: {self.Country_Name}, {self.Region}, \
            {self.IncomeGroup}, {self.Country_Code}, {self.Indicator_Name}, \
            {self.year_1995}, {self.year_1996}, {self.year_1997}, \
            {self.year_1998}, {self.year_1999}, {self.year_2000}, \
            {self.year_2001}, {self.year_2002}, {self.year_2003}, \
            {self.year_2004}, {self.year_2005}, {self.year_2006}, \
            {self.year_2007}, {self.year_2008}, {self.year_2009}, \
            {self.year_2010}, {self.year_2011}, {self.year_2012}, \
            {self.year_2013}, {self.year_2014}, {self.year_2015}, \
            {self.year_2016}, {self.year_2017}, {self.year_2018}, \
            {self.year_2019}, {self.year_2020}, \
            {self.Average_10year_in_tourist_arrivals}, \
            {self.Max_number_of_arrivals}, {self.Minimum_number_of_arrivals}, \
            {self.Percent_drop_2019_to_2020}, \
            >"

    def to_dict(self):
        """
        Sub-function creates column names dictionary.

        Used for easier serializing to JSON and testing.

        Args:
            self.
        Returns:
            Column names dictionary.
        """
        return {
            "Country_Name": self.Country_Name,
            "Region": self.Region,
            "IncomeGroup": self.IncomeGroup,
            "Country_Code": self.Country_Code,
            "Indicator_Name": self.Indicator_Name,
            "year_1995": self.year_1995,
            "year_1996": self.year_1996,
            "year_1997": self.year_1997,
            "year_1998": self.year_1998,
            "year_1999": self.year_1999,
            "year_2000": self.year_2000,
            "year_2001": self.year_2001,
            "year_2002": self.year_2002,
            "year_2003": self.year_2003,
            "year_2004": self.year_2004,
            "year_2005": self.year_2005,
            "year_2006": self.year_2006,
            "year_2007": self.year_2007,
            "year_2008": self.year_2008,
            "year_2009": self.year_2009,
            "year_2010": self.year_2010,
            "year_2011": self.year_2011,
            "year_2012": self.year_2012,
            "year_2013": self.year_2013,
            "year_2014": self.year_2014,
            "year_2015": self.year_2015,
            "year_2016": self.year_2016,
            "year_2017": self.year_2017,
            "year_2018": self.year_2018,
            "year_2019": self.year_2019,
            "year_2020": self.year_2020,
            "Average_10year_in_tourist_arrivals":
                self.Average_10year_in_tourist_arrivals,
            "Max_number_of_arrivals": self.Max_number_of_arrivals,
            "Minimum_number_of_arrivals": self.Minimum_number_of_arrivals,
            "Percent_drop_2019_to_2020": self.Percent_drop_2019_to_2020,
        }
