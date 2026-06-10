
mysql> use work
Database changed
mysql> create table student(
    -> id INT,
    -> name TEXT,
    -> age INT,
    -> score INT);
Query OK, 0 rows affected (0.26 sec)

mysql> insert into student values(1,"doniyor",19,90),
    -> (2,"ali",20,80),
    -> (3,"sarvar",19,70),
    -> (4,"sherzod",19,60),
    -> (5,"vali",20,99);
Query OK, 5 rows affected (0.10 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from students
    -> ;
ERROR 1146 (42S02): Table 'work.students' doesn't exist
mysql> select * from student;
+------+---------+------+-------+
| id   | name    | age  | score |
+------+---------+------+-------+
|    1 | doniyor |   19 |    90 |
|    2 | ali     |   20 |    80 |
|    3 | sarvar  |   19 |    70 |
|    4 | sherzod |   19 |    60 |
|    5 | vali    |   20 |    99 |
+------+---------+------+-------+
5 rows in set (0.01 sec)

mysql> select * from student where score >=90 and score <=101  order by name;
+------+---------+------+-------+
| id   | name    | age  | score |
+------+---------+------+-------+
|    1 | doniyor |   19 |    90 |
|    5 | vali    |   20 |    99 |
+------+---------+------+-------+
2 rows in set (0.07 sec)

mysql>  select * from student where score>=70 and score<=90 order by age desc;
+------+---------+------+-------+
| id   | name    | age  | score |
+------+---------+------+-------+
|    2 | ali     |   20 |    80 |
|    1 | doniyor |   19 |    90 |
|    3 | sarvar  |   19 |    70 |
+------+---------+------+-------+
3 rows in set (0.05 sec)

mysql> select * from student where score>=60 and score <=70 order by score;
+------+---------+------+-------+
| id   | name    | age  | score |
+------+---------+------+-------+
|    4 | sherzod |   19 |    60 |
|    3 | sarvar  |   19 |    70 |
+------+---------+------+-------+
2 rows in set (0.00 sec)

mysql> create database MILLIY_TAOMLAR
    -> ;
Query OK, 1 row affected (0.06 sec)

mysql> USE MILLIY_TAOMLAR;
Database changed
mysql> create table food(
    -> id int,
    -> food_name text,
    -> food_ingredients text);
Query OK, 0 rows affected (0.11 sec)

mysql> insert into food values(1,"osh","guruch"),
    -> (2,"manti","gosht"),
    -> (3,"sushi","guruch"),
    -> (4,"honim","kartoshka"),
    -> (5,"gampan","guruch"),
    -> (6,"chuchvara","sabzi"),
    -> (7,"waguri","tovuq"),
    -> (8,lagmon","baqlajon"),
    "> :
    "> ;
    "> ;
    ">
    ">
    ">
    ">
    "> (3,"sushi","guruch");
    "> "'
    '> '
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '","baqlajon"),
:
;
;




(3,"sushi","guruch");
"'
'' at line 8
mysql> insert into food values(1,"osh","guruch"),
    ->     -> (2,"manti","gosht"),
    ->     -> (3,"sushi","guruch"),
    ->     -> (4,"honim","kartoshka"),
    ->     -> (5,"gampan","guruch"),
    ->     -> (6,"chuchvara","sabzi"),
    ->     -> (7,"waguri","tovuq"),
    ->     -> (8,"lagmon","baqlajon"),
    -> "
    "> ;
    "> at line 8
    "> " '
    '> '
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '-> (2,"manti","gosht"),
    -> (3,"sushi","guruch"),
    -> (4,"honim","kartoshk' at line 2
mysql> insert into food values(1,"osh","guruch"),
    -> (2,"manti","gosht"),
    ->      (3,"sushi","guruch"),
    ->      (4,"honim","kartoshka"),
    ->      (5,"gampan","guruch"),
    ->      (6,"chuchvara","sabzi"),
    ->      (7,"waguri","tovuq"),
    ->      (8,"lagmon","baqlajon"),
    -> (9,"shorva","karam")
    -> (10,"shashlik","qiyma");
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(10,"shashlik","qiyma")' at line 10
mysql> insert into food values(1,"osh","guruch"),
    -> (2,"manti","gosht"),
    -> (3,"sushi","guruch"),
    -> (4,"honim","kartoshka"),
    -> (5,"gampan","guruch"),
    -> (6,"chuchvara","sabzi"),
    -> (7,"waguri","tovuq"),
    -> (8,"lagmon","baqlajon"),
    -> (9,"shashlik","qiyma"),
    -> (10,"shorva","guruch");
Query OK, 10 rows affected (0.07 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> select * from food where food_name LIKE "%a";
+------+-----------+------------------+
| id   | food_name | food_ingredients |
+------+-----------+------------------+
|    6 | chuchvara | sabzi            |
|   10 | shorva    | guruch           |
+------+-----------+------------------+
2 rows in set (0.07 sec)

mysql> select * from food where food_ingredients like "guruch";
+------+-----------+------------------+
| id   | food_name | food_ingredients |
+------+-----------+------------------+
|    1 | osh       | guruch           |
|    3 | sushi     | guruch           |
|    5 | gampan    | guruch           |
|   10 | shorva    | guruch           |
+------+-----------+------------------+
4 rows in set (0.00 sec)