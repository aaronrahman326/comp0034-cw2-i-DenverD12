"""For creating the database from csv."""
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, types


# Define the database file name and location
db_tourism_hotels_file = Path(__file__).parent.joinpath("tourism_hotels.db")

# Create a connection to file as a SQLite database
# (automatically creates file if it doesn't exist)
engine = create_engine("sqlite:///" + str(db_tourism_hotels_file), echo=False)

# Read the tourism_arrivals_prepared data to a pandas dataframe
tourism_arrivals_prepared_file = Path(__file__).parent.joinpath(
    "Tourism_arrivals_prepared.csv"
)
tourism_arrivals_prepared = pd.read_csv(tourism_arrivals_prepared_file)

# Write the data to tables in a sqlite database
dtype_tourism = {
    "Country Name": types.TEXT(),
    "Region": types.TEXT(),
    "IncomeGroup": types.TEXT(),
    "Country Code": types.TEXT(),
    "Indicator Name": types.TEXT(),
    "1995": types.FLOAT(),
    "1996": types.FLOAT(),
    "1997": types.FLOAT(),
    "1998": types.FLOAT(),
    "1999": types.FLOAT(),
    "2000": types.FLOAT(),
    "2001": types.FLOAT(),
    "2002": types.FLOAT(),
    "2003": types.FLOAT(),
    "2004": types.FLOAT(),
    "2005": types.FLOAT(),
    "2006": types.FLOAT(),
    "2007": types.FLOAT(),
    "2008": types.FLOAT(),
    "2009": types.FLOAT(),
    "2010": types.FLOAT(),
    "2011": types.FLOAT(),
    "2012": types.FLOAT(),
    "2013": types.FLOAT(),
    "2014": types.FLOAT(),
    "2015": types.FLOAT(),
    "2016": types.FLOAT(),
    "2017": types.FLOAT(),
    "2018": types.FLOAT(),
    "2019": types.FLOAT(),
    "2020": types.FLOAT(),
    "10-year Average in tourist arrivals": types.FLOAT(),
    "Max number of arrivals": types.FLOAT(),
    "Minimum number of arrivals": types.FLOAT(),
    "Percent drop 2019 to 2020": types.TEXT(),
}

# Create SQL database from prepared csv file
tourism_arrivals_prepared.to_sql(
    "tourism_arrivals",
    engine,
    if_exists="append",
    index=False,
    dtype=dtype_tourism,
)
