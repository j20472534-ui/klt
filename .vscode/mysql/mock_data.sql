 create database kutubxona;
 use kutubxona
Database changed
 create table books(
          bookID int, AUTO_INCREMENT primary key,
          title varchar(200) NOT NULL,
          author varchar(100) NOT NULL,
          genre varchar(50) NOT NULL,
          year_published int, NOT NULL,
          pageCount int, default 0,
          price decimal(6,2) default 0,
          avaliable boolean, default true);,
     title varchar(200) NOT NULL,
     author varchar(100) NOT NULL at line 2
 create table books(
          bookID int AUTO_INCREMENT primary key,
          title varchar(100) NOT NULL,
          author varchar(100) NOT NULL,
          genre varchar(50) NOT NULL,
          year_published int  NOT NULL,
          pageCount int  default 0,
          price decimal(6,2) default 0,
          avaliable boolean default true);
 insert into books values(
     1,"phyton","aziz","it",2019,200,100,true)
     (2,"c","sardor","it",2020,300,200,true),
     (3,"mysql","doniyor","data",2025,170,290,true),
     (4,"html","ali","design",2026,180,,300,true),
     (5,"smm","vali","marketing",2020,192,800,true);
  '(2,"c","sardor","it",2020,300,200,true),
(3,"mysql","doniyor","data",2025,170,29' at line 3
 insert into books values
               (1,"phyton","aziz","it",2019,200,100,true),
               (2,"c","sardor","it",2020,300,200,true),
               (3,"mysql","doniyor","data",2025,170,290,true),
               (4,"html","ali","design",2026,180,300,true),
               (5,"smm","vali","marketing",2020,192,800,true);
 OK, 5 rows affected (0.14 sec)
Records: 5  Duplicates: 0  Warnings: 0

 select * from books where year_published>2015;
+--------+--------+---------+-----------+----------------+-----------+--------+-----------+
| bookID | title  | author  | genre     | year_published | pageCount | price  | avaliable |
+--------+--------+---------+-----------+----------------+-----------+--------+-----------+
|      1 | phyton | aziz    | it        |           2019 |       200 | 100.00 |         1 |
|      2 | c      | sardor  | it        |           2020 |       300 | 200.00 |         1 |
|      3 | mysql  | doniyor | data      |           2025 |       170 | 290.00 |         1 |
|      4 | html   | ali     | design    |           2026 |       180 | 300.00 |         1 |
|      5 | smm    | vali    | marketing |           2020 |       192 | 800.00 |         1 |
+--------+--------+---------+-----------+----------------+-----------+--------+-----------+
5 rows in set (0.06 sec)

 insert into books values
               ("phyton","aziz","it",2019,200,100),
               ("c","sardor","it",2020,300,200),
               ("mysql","doniyor","data",2025,170,290),
               ("html","ali","design",2026,180,300),
               ("smm","vali","marketing",2020,192,800);
 1136 (21S01): Column count doesnt match value count at row 1
 select max(*) from students limit 3
     ;

 select * from books where max(pageCount) limit 3;
 1111 (HY000): Invalid use of group function
 select * from books max(pageCount) limit(3);
  
 select * from books max(pageCount) limit 3;
  
 select max(pageCount) from books  limit 3;
+----------------+
| max(pageCount) |
+----------------+
|            300 |
+----------------+
1 row in set (0.01 sec)

 select title,max(pageCount) from books  limit 3;

 select max(pageCount) from books order by pageCount limit 3;
+----------------+
| max(pageCount) |
+----------------+
|            300 |
+----------------+
1 row in set (0.04 sec)

 select title max(pageCount) from books order by pageCount limit 3;
 select *  from books order by pageCount desc limit 3;
+--------+--------+--------+-----------+----------------+-----------+--------+-----------+
| bookID | title  | author | genre     | year_published | pageCount | price  | avaliable |
+--------+--------+--------+-----------+----------------+-----------+--------+-----------+
|      2 | c      | sardor | it        |           2020 |       300 | 200.00 |         1 |
|      1 | phyton | aziz   | it        |           2019 |       200 | 100.00 |         1 |
|      5 | smm    | vali   | marketing |           2020 |       192 | 800.00 |         1 |
+--------+--------+--------+-----------+----------------+-----------+--------+-----------+
3 rows in set (0.03 sec)

 select *  from books order by genre;
+--------+--------+---------+-----------+----------------+-----------+--------+-----------+
| bookID | title  | author  | genre     | year_published | pageCount | price  | avaliable |
+--------+--------+---------+-----------+----------------+-----------+--------+-----------+
|      3 | mysql  | doniyor | data      |           2025 |       170 | 290.00 |         1 |
|      4 | html   | ali     | design    |           2026 |       180 | 300.00 |         1 |
|      1 | phyton | aziz    | it        |           2019 |       200 | 100.00 |         1 |
|      2 | c      | sardor  | it        |           2020 |       300 | 200.00 |         1 |
|      5 | smm    | vali    | marketing |           2020 |       192 | 800.00 |         1 |
+--------+--------+---------+-----------+----------------+-----------+--------+-----------+ ````