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
df.to_csv(
    "outputs/public_dashboard.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Public dashboard CSV updated successfully")