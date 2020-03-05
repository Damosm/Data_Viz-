import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import sqlite3
import os
import plotly.express as px
import base64


conn = sqlite3.connect(r'C:/Users/Utilisateur/Documents/python/Data_Viz-/db\database_update.db')
c = conn.cursor()


df_avant_medec_pay = pd.DataFrame(c.execute("select benef_nom, benef_prenom, sum(avant_montant_ttc), benef_ville from avantage where qualite = 'Médecin' and benef_nom != 'MANDOORAH' group by 1 order by 3 desc limit 20;"),columns=['Noms','Prenoms','Avantages','Villes'])

df_avant_nb_medecin_ville = pd.DataFrame(c.execute("select qualite, benef_ville, count(qualite) as nb  from avantage where qualite = 'Médecin' group by 2 order by 3 desc limit 20;"))



df_remu_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_remu_pays = df_remu_pays.fillna('')
df_remu_pays = df_remu_pays[df_remu_pays[0]!='']
########################################################################################
df_conv_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_conv_pays = df_conv_pays.fillna('')
df_conv_pays = df_conv_pays[df_conv_pays[0]!='']
########################################################################################
df_avant_pays = pd.DataFrame(c.execute("select  pays, count(pays) as total  from remuneration group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_avant_pays = df_avant_pays.fillna('')
df_avant_pays = df_avant_pays[df_avant_pays[0]!='']
########################################################################################



df_convention_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM convention group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_convention_qualite = df_convention_qualite.fillna('')
df_convention_qualite = df_convention_qualite[df_convention_qualite[0]!='']
########################################################################################
df_remu_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM remuneration group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_remu_qualite = df_remu_qualite.fillna('')
df_remu_qualite = df_remu_qualite[df_remu_qualite[0]!='']
########################################################################################
df_avant_qualite = pd.DataFrame(c.execute("SELECT qualite, COUNT(qualite) FROM avantage group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_avant_qualite = df_avant_qualite.fillna('')
df_avant_qualite = df_avant_qualite[df_avant_qualite[0]!='']
########################################################################################


df_remu_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(remu_montant_ttc) as total from remuneration group by 1 order by 2 desc limit 20;"))
df_convention_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(conv_montant_ttc) as total from convention group by 1 order by 2 desc limit 20;"))
df_avant_pay = pd.DataFrame(c.execute("select denomination_sociale, sum(avant_montant_ttc) as total from avantage group by 1 order by 2 desc limit 20;"))

df_moy_avant_pays = pd.DataFrame(c.execute("select qualite, avg(avant_montant_ttc) from avantage group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_moy_avant_pays = df_moy_avant_pays.fillna('')
df_moy_avant_pays = df_moy_avant_pays[df_moy_avant_pays[0]!='']
########################################################################################
df_moy_remu_pays = pd.DataFrame(c.execute("select qualite, avg(remu_montant_ttc) from remuneration group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_moy_remu_pays = df_moy_remu_pays.fillna('')
df_moy_remu_pays = df_moy_remu_pays[df_moy_remu_pays[0]!='']
########################################################################################
df_moy_conv_pays = pd.DataFrame(c.execute("select qualite, avg(conv_montant_ttc) from convention group by 1 order by 2 desc;"))
# suppression valeurs nulls############################################################
df_moy_conv_pays = df_moy_conv_pays.fillna('')
df_moy_conv_pays = df_moy_conv_pays[df_moy_conv_pays[0]!='']
########################################################################################


#pie moyenne pays#######################################
fig1 = px.pie(df_moy_avant_pays, values=1, names=0)
fig2 = px.pie(df_moy_remu_pays, values=1, names=0)
fig3 = px.pie(df_moy_conv_pays, values=1, names=0)
###########################################################

#bar somme ttc par entreprise#######################################
fig4 = px.bar(df_avant_pay, x=0, y=1, color=0)
fig5 = px.bar(df_remu_pay, x=0, y=1, color=0)
fig6 = px.bar(df_convention_pay, x=0, y=1, color=1)
#####################################################################

#bar somme ttc par entreprise#######################################
fig7 = px.pie(df_avant_qualite, values=1, names=0)
fig8 = px.pie(df_remu_qualite, values=1, names=0)
fig9 = px.pie(df_convention_qualite, values=1, names=0)
#####################################################################

#bar somme ttc par entreprise#######################################
#fig10 = px.scatter(df_avant_pays, x="sepal_width", y="sepal_length", color="species", size='petal_length', hover_data=['petal_width'])
# fig11 = px.pie(df_remu_pays, values=1, names=0)
# fig12 = px.pie(df_conv_pays, values=1, names=0)
#####################################################################


#bar nb de medecins par ville dans avantages############################
fig10 = px.bar(df_avant_nb_medecin_ville, x=1, y=2, color=1)


# medecin ayant percu le plsu d'avantage
fig11 = go.Figure(data=[go.Table(
    header=dict(values=list(df_avant_medec_pay.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_avant_medec_pay.Noms, df_avant_medec_pay.Prenoms, df_avant_medec_pay.Avantages, df_avant_medec_pay.Villes],
               fill_color='lavender',
               align='left'))
])






external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Répartition des avantages par secteurs professionnels'),
    dcc.Graph(
        id='conv_pro',
        figure=fig1
    ),
    
    html.Div(children=[
        html.H1(children='Répartion des rémunérations par secteurs professionnels'),
        dcc.Graph(
            id='remu_pro',
            figure=fig2
        )
    ]),
    html.Div(children=[
        html.H1(children='Répartion des conventions par secteurs professionnels'),
        dcc.Graph(
            id='moy_pro',
            figure=fig3
        )
        
    ]),
    html.H5(children='les 1ers bénéficiaires sont les chirurgiens dentiste, suivis des aides-soignants et des techniciens de laboratoires.'), 
    
    html.Div(children=[
        html.H1(children='Avantages payés par entreprise en Millions'),
        dcc.Graph(
            id='avan_entre',
            figure=fig4
        )
    ]),
    html.Div(children=[
        html.H1(children='Remunerations payées par entreprise en Millions'),
        dcc.Graph(
            id='remu_entre',
            figure=fig5
        )
    ]),
    
    
    html.Div(children=[
        html.H1(children='Conventions payées par entreprise en Millions'),
        dcc.Graph(
            id='conv_entre',
            figure=fig6
        )
    ]),
    html.H5(children='La première entreprise française, à rémunérer différents corps médicaux est SANOFI. En premier avec sa branche Sanofi Recherche et développement pour un montant de 308 Millions, suivi de SANOFI France avec 173 Millions et SANOFI GROUPE avec 126 Millions.'),
    
    html.Div(children=[
        html.H1(children='Avantages par professions en Millions'),
        dcc.Graph(
            id='anv_qualite',
            figure=fig7
        )
    ]),
    html.Div(children=[
        html.H1(children='Remunérations par professions en Millions'),
        dcc.Graph(
            id='remu_qualite',
            figure=fig8
        )
    ]),
    html.Div(children=[
        html.H1(children='Conventions par professions en Millions'),
        dcc.Graph(
            id='conv_qualite',
            figure=fig9
        )
    ]),
    html.H5(children='Nous constatons que, ce sont les médecins qui perçoivent les plus grandes sommes d’argents, mais que ce sont les physiciens médicaux, qui perçoivent le plus d’avantages.'),
    html.Div(children=[
        html.H1(children='Répartition par villes des médecins ayant perçu des avantages'),
        dcc.Graph(
            id='avan_med',
            figure=fig10
        )
    ]),
    html.H5(children='Nous pouvons remarquer que c’est à Paris que les professionnels de santé perçoivent le plus d’avantages, suivi de Marseille et Toulouse. Il y a une grande différence d’avantages entre Paris et le reste des autres villes de France.'),
    html.Div(children=[
        html.H1(children="Liste des médecins ayant perçu le plus d'avantages"),
        dcc.Graph(
            id='percu_med',
            figure=fig11
        )
    ]),
    html.Img(src=app.get_asset_url('image.jpg'))
])
if __name__ == '__main__':
    app.run_server(debug=True)