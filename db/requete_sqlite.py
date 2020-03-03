import sqlite3
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
qry = open(os.path.join('select * from avantage limit 10'), 'r').read()
conn = sqlite3.connect(os.path.join(dir_path, 'database.db'))
c = conn.cursor()
c.execute(qry)
conn.commit()
c.close()
conn.close()