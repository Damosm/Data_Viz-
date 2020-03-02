import sqlite3

conn = sqlite3.connect('db/remuneration.sqlite')
c = conn.cursor()

c.execute("SELECT * FROM MLS;")
print(c.fetchall())