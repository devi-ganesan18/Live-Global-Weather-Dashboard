USE weather_analysis;

CREATE VIEW v_weather_hourly AS
SELECT city, temperature, humidity, wind_speed, rain_mm,
       weather_condition, lat, lon, recorded_at,
       DATE(recorded_at) AS record_date
FROM weather_metrics;

CREATE VIEW v_daily_summary AS
SELECT city, DATE(recorded_at) AS record_date,
       AVG(temperature) AS avg_temp, MAX(temperature) AS max_temp,
       AVG(humidity) AS avg_humidity, SUM(rain_mm) AS total_rain
FROM weather_metrics
GROUP BY city, DATE(recorded_at);