use work

CREATE TABLE computers (
    id INT,
    brand TEXT,
    model TEXT,
    cpu TEXT,
    frequency REAL,
    ram INT,
    os TEXT,
    price INT
);

INSERT INTO computers (brand, model, cpu, frequency, ram, os, price) VALUES
('Apple', 'MacBook Pro', 'Intel Core i7', 3.5, 16, 'macOS', 2500),
('Apple', 'MacBook Air', 'Intel Core i5', 2.8, 8, 'macOS', 1200),
('ASUS', 'ZenBook 14', 'Intel Core i5', 2.4, 8, 'Windows 10', 850),
('ASUS', 'VivoBook 15', 'AMD Ryzen 5', 3.2, 16, 'Windows 10', 650),
('Dell', 'XPS 13', 'Intel Core i7', 3.9, 16, 'Windows 10', 1800),
('Dell', 'Inspiron 15', 'Intel Core i5', 2.5, 8, 'Windows 10', 700),
('HP', 'Pavilion 15', 'AMD Ryzen 5', 2.1, 8, 'Windows 10', 550),
('HP', 'EliteBook 840', 'Intel Core i7', 3.1, 16, 'Windows 10', 1400),
('Lenovo', 'ThinkPad X1', 'Intel Core i7', 3.8, 16, 'Ubuntu 20.04', 1900),
('Lenovo', 'IdeaPad 3', 'AMD Ryzen 5', 1.8, 4, 'Windows 10', 450),
('Apple', 'MacBook Pro 16', 'Intel Core i9', 3.6, 16, 'macOS', 3000),
('ASUS', 'ROG Zephyrus', 'AMD Ryzen 5', 3.0, 16, 'Windows 10', 1600),
('Dell', 'Latitude 5420', 'Intel Core i5', 2.6, 8, 'Ubuntu 20.04', 950),
('HP', 'Spectre x360', 'Intel Core i7', 3.3, 16, 'Windows 10', 1700),
('Lenovo', 'Legion 5', 'AMD Ryzen 5', 3.1, 16, 'Windows 10', 1100),
('Apple', 'MacBook Air M1', 'Intel Core i5', 2.0, 8, 'macOS', 999),
('ASUS', 'ExpertBook B9', 'Intel Core i7', 2.9, 16, 'Windows 10', 1350),
('Dell', 'G15 Gaming', 'Intel Core i7', 3.4, 16, 'Windows 10', 1250),
('HP', 'Omen 15', 'Intel Core i7', 2.3, 8, 'Windows 10', 1150),
('Lenovo', 'Yoga Slim 7', 'AMD Ryzen 5', 2.7, 8, 'Windows 10', 880);

select * from computers order by price desc limit 1;
select * from computers order by price  limit 1;
select frequency from computers where price between 400 and 1000 and  cpu like '%intel%';
select count(*) from computers where brand like '%apple%';
select * from computers where os = 'Windows 10' and ram = 8 and brand = 'ASUS' order by price;
