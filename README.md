# Live Global Weather Dashboard

An end-to-end data pipeline and Power BI dashboard that collects live weather data
for five cities every hour and visualizes trends, conditions and locations.

## Pipeline
OpenWeather API -> Python -> MySQL -> SQL Views -> Power BI

## Tools
Python (requests, pandas, SQLAlchemy), MySQL, Excel, Windows Task Scheduler, Power BI (DAX)

## Dataset
- Source: OpenWeather Current Weather API
- Cities: New York, London, Tokyo, Sydney, Mumbai
- Frequency: hourly (Windows Task Scheduler)
- Columns: city, temperature, humidity, wind_speed, rain_mm,
  weather_condition, lat, lon, recorded_at

## Project Steps
1. Get an OpenWeather API key.
2. Create the MySQL database and table (`01_create_table.sql`).
3. Run `weather.py` to fetch data and store it in MySQL.
4. Validate data in Excel (outliers, PivotTable of average temperature).
5. Schedule `weather.py` hourly with Task Scheduler to build history.
6. Create SQL views with data quality filters (`02_create_views.sql`).
7. Connect Power BI to MySQL and build DAX measures.
8. Design the dashboard.

## DAX Measures
Avg Temp, Avg Humidity, Avg Wind, Total Rain, Rainy Readings,
Last Updated, Latest Temp, Temp Anomaly

## Dashboard
- KPI cards: Latest Temperature, Avg Humidity, Avg Wind Speed, Total Rain
- Temperature trend by city (line chart)
- Latest temperature by location (map)
- Weather condition share (donut)
- Average temperature by city (bar chart)
- Slicers: city and date

## How to Run
1. Install: `pip install requests pandas sqlalchemy pymysql`
2. Run `01_create_table.sql` and `02_create_views.sql` in MySQL Workbench.
3. In `weather.py`, set `API_KEY` and `PASSWORD`.
4. Run `python weather.py`.
5. Open `Weather_Analysis_Dashboard.pbix` in Power BI Desktop and click Refresh.

## Limitations
- Data is collected only while the laptop is on. In production this would run on a cloud server.
- Power BI refresh is manual (auto-refresh needs Power BI Service and a gateway).
## Author
<Unga peru>
