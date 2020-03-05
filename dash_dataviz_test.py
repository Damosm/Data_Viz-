import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import sqlite3
import os
import plotly.express as px


conn = sqlite3.connect(r'C:\Users\utilisateur\Documents\Python\Data_Viz-\db\database_update.db')
c = conn.cursor()

# df_avant_medec_pay = pd.DataFrame(c.execute("select benef_nom, benef_prenom, sum(avant_montant_ttc), benef_ville from avantage where qualite = 'Médecin' and benef_nom != 'MANDOORAH' group by 1 order by 3 desc limit 20;"),columns=['Noms','Prenoms','Avantages','Villes'])

# df_avant_nb_medecin_ville = pd.DataFrame(c.execute("select qualite, benef_ville, count(qualite) as nb  from avantage where qualite = 'Médecin' group by 2 order by 3 desc limit 20;"))


# df_remu_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration group by 1 order by 2 desc limit 20;"))
df_remu_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration where pays in ('RÉUNION','MARTINIQUE','GUADELOUPE','GUYANE FRANÇAISE','NOUVELLE-CALÉDONIE','POLYNÉSIE FRANÇAISE','MONACO','MONACO','BELGIQUE','MAROC','SUISSE') group by 1 order by 1 desc limit 20;"),columns=['Pays','Remu'])
# suppression valeurs nulls############################################################
df_remu_pays = df_remu_pays.fillna('')
df_remu_pays = df_remu_pays[df_remu_pays['Pays']!='']
# ########################################################################################
# df_conv_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from convention group by 1 order by 2 desc limit 20;"))
df_conv_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from convention  where pays in ('RÉUNION','MARTINIQUE','GUADELOUPE','GUYANE FRANÇAISE','NOUVELLE-CALÉDONIE','POLYNÉSIE FRANÇAISE','MONACO','BELGIQUE','MAROC','SUISSE') group by 1 order by 1 desc limit 20;"),columns=['Pays','Conv'])
# suppression valeurs nulls############################################################
df_conv_pays = df_conv_pays.fillna('')
df_conv_pays = df_conv_pays[df_conv_pays['Pays']!='']
########################################################################################
# df_avant_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from avantage group by 1 order by 2 desc limit 20;"))
df_avant_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from avantage  where pays in ('RÉUNION','MARTINIQUE','GUADELOUPE','GUYANE FRANÇAISE','NOUVELLE-CALÉDONIE','POLYNÉSIE FRANÇAISE','MONACO','BELGIQUE','MAROC','SUISSE') group by 1 order by 1 desc limit 20;"),columns=['Pays','Avant'])
# suppression valeurs nulls############################################################
df_avant_pays = df_avant_pays.fillna('')
df_avant_pays = df_avant_pays[df_avant_pays['Pays']!='']
########################################################################################
# print (df_remu_pays)
# print (df_conv_pays)
# print (df_avant_pays)

# df = pd.concat([df_remu_pays,df_conv_pays[1],df_avant_pays[1]])
df = pd.concat([df_remu_pays, df_conv_pays['Conv'].reindex(df_remu_pays.index)], axis=1)
df = pd.concat([df, df_avant_pays['Avant'].reindex(df.index)], axis=1)

# df = pd.DataFrame(df, columns=['Pays','Remu','Conv','Avant'])

# where pays in ('FRANCE','RÉUNION','MARTINIQUE','GUADELOUPE','GUYANE FRANÇAISE','NOUVELLE-CALÉDONIE','POLYNÉSIE FRANÇAISE','MONACO','MONACO','BELGIQUE','MAROC','SUISSE','ALGÉRIE','GUYANA','GUINÉE','TUNISIE')
# df_convention_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM convention group by 1 order by 2 desc;"))
# # suppression valeurs nulls############################################################
# df_convention_qualite = df_convention_qualite.fillna('')
# df_convention_qualite = df_convention_qualite[df_convention_qualite[0]!='']
# ########################################################################################
# df_remu_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM remuneration group by 1 order by 2 desc;"))
# # suppression valeurs nulls############################################################
# df_remu_qualite = df_remu_qualite.fillna('')
# df_remu_qualite = df_remu_qualite[df_remu_qualite[0]!='']
# ########################################################################################
# df_avant_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM avantage group by 1 order by 2 desc;"))
# # suppression valeurs nulls############################################################
# df_avant_qualite = df_avant_qualite.fillna('')
# df_avant_qualite = df_avant_qualite[df_avant_qualite[0]!='']
# ########################################################################################


# df_remu_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(remu_montant_ttc) as total from remuneration group by 1 order by 2 desc limit 20;"))
# df_convention_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(conv_montant_ttc) as total from convention group by 1 order by 2 desc limit 20;"))
# df_avant_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(avant_montant_ttc) as total from avantage group by 1 order by 2 desc limit 20;"))

# df_moy_avant_pays = pd.DataFrame(c.execute("select qualite, avg(avant_montant_ttc) from avantage group by 1 order by 2 desc;"))
# # suppression valeurs nulls############################################################
# df_moy_avant_pays = df_moy_avant_pays.fillna('')
# df_moy_avant_pays = df_moy_avant_pays[df_moy_avant_pays[0]!='']
# ########################################################################################
# df_moy_remu_pays = pd.DataFrame(c.execute("select qualite, avg(remu_montant_ttc) from remuneration group by 1 order by 2 desc;"))
# # suppression valeurs nulls############################################################
# df_moy_remu_pays = df_moy_remu_pays.fillna('')
# df_moy_remu_pays = df_moy_remu_pays[df_moy_remu_pays[0]!='']
# ########################################################################################
# df_moy_conv_pays = pd.DataFrame(c.execute("select qualite, avg(conv_montant_ttc) from convention group by 1 order by 2 desc;"))
# # suppression valeurs nulls############################################################
# df_moy_conv_pays = df_moy_conv_pays.fillna('')
# df_moy_conv_pays = df_moy_conv_pays[df_moy_conv_pays[0]!='']
# ########################################################################################

conn.commit()
c.close() 
conn.close()  
# #pie moyenne pays#######################################
# fig1 = px.pie(df_moy_avant_pays, values=1, names=0)
# fig = px.pie(df_moy_remu_pays, values=1, names=0)
# fig3 = px.pie(df_moy_conv_pays, values=1, names=0)
# ###########################################################

# #bar somme ttc par entreprise#######################################
# fig4 = px.bar(df_avant_pay, x=0, y=1)
# fig5 = px.bar(df_remu_pay, x=0, y=1)
# fig6 = px.bar(df_convention_pay, x=0, y=1)
# #####################################################################

# #bar somme ttc par entreprise#######################################
# fig7 = px.bar(df_avant_qualite, x=0, y=1)
# fig8 = px.bar(df_remu_qualite, x=0, y=1)
# fig9 = px.bar(df_convention_qualite, x=0, y=1)
# #####################################################################

# #bar somme ttc par entreprise#######################################
# fig10 = px.bar(df_avant_pays, x=0, y=1)
# fig11 = px.bar(df_remu_pays, x=0, y=1)
# fig12 = px.bar(df_conv_pays, x=0, y=1)
# #####################################################################



# #bar nb de medecins par ville dans avantages############################
# fig13 = px.bar(df_avant_nb_medecin_ville, x=1, y=2)

# fig14 = go.Figure(data=[go.Table(
#     header=dict(values=list(df_avant_medec_pay.columns),
#                 fill_color='paleturquoise',
#                 align='left'),
#     cells=dict(values=[df_avant_medec_pay.Noms, df_avant_medec_pay.Prenoms, df_avant_medec_pay.Avantages, df_avant_medec_pay.Villes],
#                fill_color='lavender',
#                align='left'))
# ])

# print(df)
fig = px.bar(df, x='Pays', y='Remu')
fig.add_bar(x=df['Pays'], y=df['Conv'])
fig.add_bar(x=df['Pays'], y=df['Avant'])


# fig1 = px.pie(df_moy_conv_pays, values=1, names=0)
# fig = px.bar_polar(df_remu_pays, r=0, theta=1, color="strength", template="plotly_dark",
#             color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()