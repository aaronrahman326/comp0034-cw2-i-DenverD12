"""For creating the database from csv."""
from pathlib import Path
import pandas as pd

# Read the tourism_arrivals_prepared data to a pandas dataframe
tourism_arrivals_prepared_file = Path(__file__).parent.joinpath("events.csv")
tourism_arrivals_prepared = pd.read_csv(tourism_arrivals_prepared_file)

print(tourism_arrivals_prepared.info())
