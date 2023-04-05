"""For creating the database from csv."""
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, types


# Define the database file name and location
db_file = Path(__file__).parent.joinpath("tourism_hotels.db")

# Create a connection to file as a SQLite database (this automatically creates the file if it doesn't exist)
engine = create_engine("sqlite:///" + str(db_file), echo=False)

# Read the noc_regions data to a pandas dataframe
# The following avoids an issue whereby entries with "NA" in the csv file are treated as null values rather than valid text 'NA' which is what we want
na_values = [
    "",
    "#N/A",
    "#N/A N/A",
    "#NA",
    "-1.#IND",
    "-1.#QNAN",
    "-NaN",
    "-nan",
    "1.#IND",
    "1.#QNAN",
    "<NA>",
    "N/A",
    "NULL",
    "NaN",
    "n/a",
    "nan",
    "null",
]
noc_file = Path(__file__).parent.joinpath("regions.csv")
# Read the data and handles the NA issue
noc_regions = pd.read_csv(noc_file, keep_default_na=False, na_values=na_values)

# Read the paralympics event data to a pandas dataframe
event_file = Path(__file__).parent.joinpath("Tourism_arrivals_prepared.csv")
paralympics = pd.read_csv(event_file)

# Write the data to tables in a sqlite database
dtype_noc = {
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
    "Percent drop 2019 to 2020": types.FLOAT(),
}

dtype_event = {
    "NOC": types.TEXT(),
    "region": types.TEXT(),
    "notes": types.TEXT(),
}

noc_regions.to_sql(
    "region", engine, if_exists="append", index=False, dtype=dtype_noc
)
paralympics.to_sql(
    "event", engine, if_exists="append", index=False, dtype=dtype_event
)
