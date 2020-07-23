import sqlite3
conn = sqlite3.connect('test.db')
import os
c=conn.cursor()
def tab():
	c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, no INTEGER, name TEXT)")
	c.execute("CREATE TABLE test2 (t2id INTEGER PRIMARY KEY, no2 INTEGER)")
def tab2():
	
	 
	c.execute("CREATE TABLE rel (rid INTEGER PRIMARY KEY, tid INTEGER, t2id INTEGER, FOREIGN KEY (tid) REFERENCES test(id), FOREIGN KEY (t2id) REFERENCES test2(id))")
def ins():
	
	
	for i in range(0,6,2):
		p=[i]
		c.execute("INSERT INTO rel (no2) VALUES (?)",p)
	conn.commit()
def sho():
	c.execute("SELECT * FROM test")
	for i in c:
		print(i)
	




c.execute("SELECT test.id ,test2.t2id,no2 FROM rel INNER JOIN test ON rel.tid=test.id INNER JOIN test2 ON rel.t2id=test2.t2id")
for i in c:
	print(i)

conn.close()