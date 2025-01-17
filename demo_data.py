# -*- coding: utf-8 -*-
"""SQL sprint challenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ebqQNV4dst9YbSudW6yequld02bhYGzb
"""

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_demo_table = """
CREATE TABLE demo (
  s VARCHAR(1),
  x INT,
  y INT)
"""

curs.execute(create_demo_table)

insert = """
  INSERT INTO demo
  VALUES
  ('g', 3, 9),
  ('v', 5, 7),
  ('f', 8, 7);"""
insert

curs.execute(insert)

conn.commit()  # We need to "save" our work for the new table/data to show up

query1 = 'SELECT count(*) FROM demo;'
print(curs.execute(query1).fetchall())

query2 = 'SELECT count(*) FROM demo WHERE x>=5 AND y>=5'
print(curs.execute(query2).fetchall())

query3 = 'SELECT count(DISTINCT y) FROM demo'
print(curs.execute(query3).fetchall())
