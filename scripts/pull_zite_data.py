import requests
import pandas as pd
from pathlib import Path

API_URL = "PUT_YOUR_ZITE_URL_HERE"

response = requests.get(API_URL)
response.raise_for_status()

data = response.json()

df = pd.json_normalize(data)

Path("outputs").mkdir(exist_ok=True)

df.to_csv("outputs/zite_data.csv", index=False)

print("CSV updated successfully")
