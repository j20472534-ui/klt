CREATE TABLE author(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE genre(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE book(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2),
    amount INT,
    a_id INT,
    g_id INT,
    FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (g_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO genre(name) VALUES("Roman"), ("Fantastika"), ("Dramma"), ("Tragediya");

INSERT INTO author(name) VALUES("Alisher Navoiy"), ("Pushkin"), ("Bobur"), ("Abdulla Qodiriy");

INSERT INTO book
    (name, price, amount, g_id, a_id) 
VALUES
    ("O'tgan kunlar", 35000, 10, 4, 1),
    ("Shaytanant", 15000, 5, 1, 3),
    ("Hamsa", 150000, 1, 2, 1),
    ("Odam bo'lish qiyin", 10000, 20, 2, 2),
    ("Diqqat", 17000, 2, 3, 4),
    ("12 yil qullikda", 10000, 2, 1, 2),
    ("Jinoyat va jazo", 17000, 8, 4, 1),
    ("Oq kechalar", 25000, 2, 3, 3),
    ("Atom Odatlar", 35000, 3, 2, 4),
    ("Yulduzli tunlar", 39000, 1, 1, 1),
    ("Dunyoning ishlari", 31000, 4, 2, 3),
    ("Kichik Shahzoda", 1000, 5, 1, 2),
    ("Kecha va Kunduz", 19000, 10, 4, 4),
    ("Bilmasvoy", 17000, 5, 2, 1);

select * from book as b
     inner join author as a
     on a.id = b.a_id;


select * from book as b
inner join author  as a 
on b.a_id = a.id
inner join genre as g 
on b.g_id = g.id;

select g.name from genre as g inner join book as b on b.g_id = g.id where b.a_id=1 group by g.name;

select a.name as autor, JSON_ARRAYAGG(g.name) as janrlar
from author as a
inner join book as b on b.a_id = a.id
inner join genre as g on b.g_id = g.id
group by a.name;

select a.name as autor, g.name as janr, count(b.id) as kitob_soni
from author as a
inner join book as b on b.a_id = a.id
inner join genre as g on b.g_id = g.id
group by a.name, g.name;

select g.name as janr, count(b.id) as soni
from genre as g
inner join book as b on b.g_id = g.id
group by g.name
order by soni desc
limit 1;


select a.name as autor, sum(b.amount) as jami_sotilgan
from author as a
inner join book as b on b.a_id = a.id
group by a.name
order by jami_sotilgan desc
limit 1;