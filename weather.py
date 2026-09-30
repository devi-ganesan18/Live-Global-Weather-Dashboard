import requests, pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

API_KEY = "8e6f72355699849c09ce8ae298e8713d"
PASSWORD = "devigyoga@1808"
cities = ["New York", "London", "Tokyo", "Sydney", "Mumbai"]
rows = []

for city in cities:
    url = "https://api.openweathermap.org/data/2.5/weather"
    r = requests.get(url, params={"q": city, "appid": API_KEY, "units": "metric"}).json()
    rows.append({
        "city": city,
        "temperature": r["main"]["temp"],
        "humidity": r["main"]["humidity"],
        "wind_speed": r["wind"]["speed"],
        "rain_mm": r.get("rain", {}).get("1h", 0),
        "weather_condition": r["weather"][0]["main"],
        "lat": r["coord"]["lat"],
        "lon": r["coord"]["lon"],
    })

df = pd.DataFrame(rows)
df["recorded_at"] = pd.Timestamp.now()
df.to_csv("weather_staging.csv", index=False)

engine = create_engine(
    f"mysql+pymysql://root:{quote_plus(PASSWORD)}@localhost:3306/weather_analysis"
)
df.to_sql("weather_metrics", engine, if_exists="append", index=False)
print("Saved", len(df), "rows")
