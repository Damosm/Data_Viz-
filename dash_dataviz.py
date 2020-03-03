import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import sqlite3
import os
import plotly.express as px


conn = sqlite3.connect(r'C:\Users\utilisateur\Documents\Python\Data_Viz-\db\database.db')
c = conn.cursor()
# df_remu_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(remu_montant_ttc) as total from remuneration group by 1 order by 2 desc limit 20;"))
# df_convention_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(conv_montant_ttc) as total from convention group by 1 order by 2 desc limit 20;"))
# df_avant_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(avant_montant_ttc) as total from avantage group by 1 order by 2 desc limit 20;"))
# df_convention_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM convention group by 1 order by 2 desc;"))
# df_remu_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM remuneration group by 1 order by 2 desc;"))
# df_avant_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM avantage group by 1 order by 2 desc;"))
# df_remu_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration group by 1 order by 2 desc;"))
# df_conv_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration group by 1 order by 2 desc;"))
# df_avant_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration group by 1 order by 2 desc;"))
# df_moy_remu_pays = pd.DataFrame(c.execute("select qualite, avg(remu_montant_ttc) from remuneration group by 1 order by 2 desc;"))
# df_moy_avant_pays = pd.DataFrame(c.execute("select qualite, avg(avant_montant_ttc) from avantage group by 1 order by 2 desc;"))
df_moy_conv_pays = pd.DataFrame(c.execute("select qualite, avg(conv_montant_ttc) from convention group by 1 order by 2 desc;"))
 

conn.commit()
c.close() 
conn.close()  


# fig = px.bar(df_avant_pay, x=0, y=1)
fig = px.pie(df_moy_conv_pays, names=0, values=1)
# fig = px.bar_polar(df_remu_pays, r=0, theta=1, color="strength", template="plotly_dark",
#             color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()