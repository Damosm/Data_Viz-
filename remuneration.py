from classes.Csv import Csv
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)

remuneration_csv = Csv('declaration_remuneration_2020_02_19_04_00', 'utf-8', ';')
df = remuneration_csv.get_data()
df.to_sql('remuneration', con=engine)

# print(engine.execute("SELECT * FROM remuneration").fetchall())