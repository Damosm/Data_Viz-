from classes.Csv import Csv
import sqlite3
import pandas as pd
from tqdm import tqdm

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def insert_with_progress(df, dbfile):
    con = sqlite3.connect(dbfile)
    chunksize = int(len(df) / 10) # 10%
    with tqdm(total=len(df)) as pbar:
        for i, cdf in enumerate(chunker(df, chunksize)):
            replace = "replace" if i == 0 else "append"
            cdf.to_sql(con=con, name="MLS", if_exists=replace, index=False)
            pbar.update(chunksize)

csv_files = {
    'declaration_remuneration_2020_02_19_04_00':'remuneration.sqlite',
    'declaration_convention_2020_02_19_04_00':'convention.sqlite',
    'declaration_avantage_2020_02_19_04_00':'avantage.sqlite',
    'entreprise_2020_02_19_04_00':'entreprise.sqlite'
}

for csv_name, db_name in csv_files.items():
    df = Csv(csv_name, 'utf-8', ';').get_data()
    insert_with_progress(df, db_name)

