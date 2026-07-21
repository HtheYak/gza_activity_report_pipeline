import os
import requests
import pandas as pd
from pathlib import Path

# Load API URL securely from GitHub Secrets
API_URL = os.environ["ZITE_API_URL"]

# Pull data from Zite API
response = requests.get(API_URL)
response.raise_for_status()

data = response.json()

# Normalize JSON into table
df = pd.json_normalize(data)

# Remove sensitive columns
columns_to_remove = [
    "Location"
]

df = df.drop(columns=columns_to_remove, errors="ignore")

# Create outputs folder if missing
Path("outputs").mkdir(exist_ok=True)

# Export cleaned public dataset
output_path = "outputs/public_dashboard.csv"

df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print("=" * 50)
print("ZITE DASHBOARD REFRESH")
print("=" * 50)
print(f"Rows exported: {len(df):,}")

if "Site ID" in df.columns:
    print(f"Unique sites: {df['Site ID'].nunique(dropna=True):,}")

if "Agency" in df.columns:
    print(f"Unique agencies: {df['Agency'].nunique(dropna=True):,}")

if "Activity date" in df.columns:
    activity_dates = pd.to_datetime(
        df["Activity date"],
        errors="coerce"
    )

    valid_dates = activity_dates.dropna()

    if not valid_dates.empty:
        print(f"Earliest activity date: {valid_dates.min().date()}")
        print(f"Latest activity date: {valid_dates.max().date()}")
    else:
        print("No valid activity dates found.")

print(f"CSV written: {output_path}")
print("=" * 50)
