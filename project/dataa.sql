CREATE DATABASE transport_routes_db;

USE transport_routes_db;

CREATE TABLE routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    route_number VARCHAR(10) NOT NULL,
    start_point VARCHAR(50) NOT NULL,
    end_point VARCHAR(50) NOT NULL,
    duration_min INT NOT NULL,
    distance_km DECIMAL(10,1) NOT NULL,
    ticket_price DECIMAL(10,2) NOT NULL,
    bus_type VARCHAR(20) NOT NULL
);

INSERT INTO routes 
(route_number, start_point, end_point, duration_min, distance_km, ticket_price, bus_type)
VALUES
('12', 'Chilonzor', 'Yunusobod', 40, 18.5, 2000.00, 'Shahar'),
('21A', 'Sergeli', 'Olmazor', 55, 24.0, 2500.00, 'Tezyurar'),
('75', 'Qo''yliq', 'Beruniy', 35, 15.2, 1800.00, 'Shahar'),
('9', 'TTZ', 'Chorsu', 28, 12.0, 1700.00, 'Elektr'),
('44', 'Yakkasaroy', 'Minor', 50, 20.5, 2300.00, 'Shahar'),
('108', 'Bektemir', 'Amir Temur', 65, 30.0, 3000.00, 'Tezyurar'),
('5B', 'Olmazor', 'Qorasuv', 45, 19.3, 2100.00, 'Elektr'),
('31', 'Sergeli', 'Chorsu', 38, 16.8, 1900.00, 'Shahar'),
('66', 'Yunusobod', 'Qo''yliq', 70, 32.5, 3200.00, 'Tezyurar'),
('18', 'Minor', 'TTZ', 25, 10.4, 1600.00, 'Elektr'),
('90', 'Chilonzor', 'Bektemir', 80, 36.0, 3500.00, 'Tezyurar'),
('27', 'Beruniy', 'Sergeli', 33, 14.7, 1850.00, 'Shahar');
SELECT *
FROM routes
ORDER BY ticket_price ASC;

SELECT *
FROM routes
ORDER BY distance_km DESC
LIMIT 3;

SELECT *
FROM routes
WHERE duration_min > 30
AND bus_type = 'Shahar';

SELECT bus_type, AVG(ticket_price) AS avg_price
FROM routes
GROUP BY bus_type;