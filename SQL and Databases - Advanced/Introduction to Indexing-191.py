## 1. Introduction ##

import sqlite3
conn = sqlite3.connect('factbook.db')
schema = conn.execute('pragma table_info(facts);').fetchall()
for e in schema:
    print(e)
conn.close()

## 3. Explain query plan ##

conn = sqlite3.connect("factbook.db")
query_plan_one = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts where area > 40000;").fetchall()
query_plan_two = conn.execute("EXPLAIN QUERY PLAN SELECT area FROM facts where area > 40000;").fetchall()
query_plan_three = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts where name='Czech Republic';").fetchall()
print(query_plan_one,query_plan_two,query_plan_three)

## 5. Time complexity ##

conn = sqlite3.connect("factbook.db")
query_plan_four = conn.execute("explain query plan Select * from facts where id=20;").fetchall()
print(query_plan_four)

## 9. All together now ##

conn = sqlite3.connect("factbook.db")
query_plan_six = conn.execute("explain query plan Select * from facts where population>10000;").fetchall()
print(query_plan_six)
conn.execute("CREATE INDEX IF NOT EXISTS pop_idx ON facts(population);")
query_plan_seven = conn.execute("explain query plan Select * from facts where population>10000;").fetchall()
print(query_plan_seven)