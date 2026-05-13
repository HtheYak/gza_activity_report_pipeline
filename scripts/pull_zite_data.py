import requests
import pandas as pd
from pathlib import Path

API_URL = "https://app.zitemanager.org/api/v2/reports-file/?report_id=6839&key=7Hzb8_zMtQsu3MJ93Vu2vliZV2I2642871045"

response = requests.get(API_URL)
response.raise_for_status()

data = response.json()

df = pd.json_normalize(data)

Path("outputs").mkdir(exist_ok=True)

df.to_csv(
    "outputs/zite_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("CSV updated successfully")
