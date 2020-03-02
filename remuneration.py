from classes.Csv import Csv

remuneration_csv = Csv('declaration_remuneration_2020_02_19_04_00', 'utf-8', ';')
df = remuneration_csv.get_data()

print(df.iloc[0])