USE weather_analysis;

CREATE TABLE weather_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    wind_speed FLOAT,
    rain_mm FLOAT,
    weather_condition VARCHAR(50),
    lat FLOAT,
    lon FLOAT,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
