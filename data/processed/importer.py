import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("hotel_booking_cleaned.csv")

# remove accidental CSV index columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# remove helper column not present in PostgreSQL table
df = df.drop(columns=["arrival_month_num"], errors="ignore")

engine = create_engine(
    "postgresql+psycopg2://postgres:admin@localhost:5432/hotel_analytics"
)

df.to_sql(
    "hotel_bookings",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(df)} rows")