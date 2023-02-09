import sqlite3

db = sqlite3.connect('students.db')

m = db.cursor()

m.execute(""" CREATE TABLE IF NOT EXISTS student(
Hobby text,
Name text,
Surname text,
Date_OF_Birth integer,
Points integer)
""")

# m.execute("INSERT INTO student  VALUES('Lionel', 'Messi', 'PSG', 30, 1985)")
# m.execute("INSERT INTO student  VALUES('Kilian', 'Mbappe', 'PSG', 7, 1998)")
# m.execute("INSERT INTO student  VALUES('Neymar ', 'Júnior', 'PSG', 10, 1992)")
# m.execute("INSERT INTO student  VALUES('Ousmane', 'Dembele', 'FC Barcelona', 7, 1997)")
# m.execute("INSERT INTO student  VALUES('Robert', 'Lewandowski', 'FC Barcelona', 9, 1988)")
# m.execute("INSERT INTO student  VALUES('Raphael', 'Dias', 'FC Barcelona', 22, 1996)")
# m.execute("INSERT INTO student  VALUES('Federico', 'Valverde', 'Real Madrid', 15, 1998)")
# m.execute("INSERT INTO student  VALUES('Karim', 'Benzema', 'Real Madrid', 9, 1987)")
# m.execute("INSERT INTO student  VALUES('ViniciusJunior', 'Junior', 'Real Madrid', 20, 2000)")
# m.execute("INSERT INTO student  VALUES('Diego', 'Maradona', 'All Stars', 10, 1960)")
# m.execute("SELECT rowid, surname FROM student WHERE LENGTH(surname) >= 10 ")
# print(m.fetchall())
# m.execute("UPDATE student SET name = 'genius' WHERE Points >= 10")
# m.execute("SELECT rowid, *   FROM student WHERE name = 'genius'")
# print(m.fetchall())
# m.execute("DELETE FROM student WHERE rowid % 2 == 0")
# db.commit()
# db.close()
