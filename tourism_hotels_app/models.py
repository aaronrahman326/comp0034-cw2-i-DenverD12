# This file is to define the model classes that will map from the database to Python classes
from tourism_hotels_app import db


## First example if you want to only provide some, not all, the fields from a class in the data
## This inherits ma.SQLAlchemySchema and you then need to state the fields that you wish to be included in the data.
# class Region(db.Model):
#     """NOC region"""

#     __tablename__ = "region"
#     NOC = db.Column(db.Text, primary_key=True)
##     region = db.Column(db.Text, nullable=False)
#     notes = db.Column(db.Text)
#     events = db.relationship("Event", back_populates="region")

#     def __repr__(self):
#         """
#         Returns the attributes of the region as a string
#         :returns str
#         """
#         clsname = self.__class__.__name__
#         return f"{clsname}: <{self.NOC}, {self.region}, {self.notes}>"


class TourismArrivals(db.Model):
    """Tourist Arrivals per year in each country"""

    __tablename__ = "tourism_arrivals"
    ## set nullable=false to ensure any attempt to enter new data in that column without specifying a value returns an error
    Country_Name = db.Column('Country Name', db.Text, nullable=False, primary_key=True)
    Region = db.Column(db.Text, nullable=False)
    IncomeGroup = db.Column(db.Text, nullable=False)
    Country_Code = db.Column('Country Code', db.Text, nullable=False)
    Indicator_Name = db.Column('Indicator Name', db.Text, nullable=False)
    year_1995 = db.Column('1995', db.Integer, nullable=False)
    year_1996 = db.Column('1996', db.Integer, nullable=False)
    year_1997 = db.Column('1997', db.Integer, nullable=False)
    year_1998 = db.Column('1998', db.Integer, nullable=False)
    year_1999 = db.Column('1999', db.Integer, nullable=False)
    year_2000 = db.Column('2000', db.Integer, nullable=False)
    year_2001 = db.Column('2001', db.Integer, nullable=False)
    year_2002 = db.Column('2002', db.Integer, nullable=False)
    year_2003 = db.Column('2003', db.Integer, nullable=False)
    year_2004 = db.Column('2004', db.Integer, nullable=False)
    year_2005 = db.Column('2005', db.Integer, nullable=False)
    year_2006 = db.Column('2006', db.Integer, nullable=False)
    year_2007 = db.Column('2007', db.Integer, nullable=False)
    year_2008 = db.Column('2008', db.Integer, nullable=False)
    year_2009 = db.Column('2009', db.Integer, nullable=False)
    year_2010 = db.Column('2010', db.Integer, nullable=False)
    year_2011 = db.Column('2011', db.Integer, nullable=False)
    year_2012 = db.Column('2012', db.Integer, nullable=False)
    year_2013 = db.Column('2013', db.Integer, nullable=False)
    year_2014 = db.Column('2014', db.Integer, nullable=False)
    year_2015 = db.Column('2015', db.Integer, nullable=False)
    year_2016 = db.Column('2016', db.Integer, nullable=False)
    year_2017 = db.Column('2017', db.Integer, nullable=False)
    year_2018 = db.Column('2018', db.Integer, nullable=False)
    year_2019 = db.Column('2019', db.Integer, nullable=False)
    year_2020 = db.Column('2020', db.Integer, nullable=False)
    Average_10year_in_tourist_arrivals = db.Column('10-year Average in tourist arrivals', db.Integer)
    Max_number_of_arrivals = db.Column('Max number of arrivals', db.Integer)
    Minimum_number_of_arrivals = db.Column('Minimum number of arrivals', db.Integer)
    Percent_drop_2019_to_2020 = db.Column('Percent drop 2019 to 2020', db.Text)

    def __repr__(self):
        """
        Returns the attributes of the country as a string
        :returns str
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
