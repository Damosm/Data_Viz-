import sqlite3
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# qry = open(os.path.join(dir_path, 'query.sql'), 'r').read()
conn = sqlite3.connect(os.path.join(dir_path, 'database.db'))
c = conn.cursor()
c.execute("select * from avantage limit 10")
conn.commit()
c.close()
conn.close()