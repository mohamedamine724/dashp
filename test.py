import dash
import dash_core_components as dcc
import dash_html_components as html

consum = []

import csv

with open('test.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         consum.append(row['consum'])

# Estils externs perquè la pàgina sigui responsive.
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] 

# Creem el "objecte" aplicació.
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Definim el Titol i subtitol.
app.layout = html.Div(children=[
    html.H1(children='Consum Elèctric'),
    html.Div(children='''Dashboard: Per controlar el consum diari.'''),

#En aquesta part generem el Dash.            
dcc.Graph(
        id='example-graph',
        figure={
        'data': [
                  {'x': ['Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres', 'Dissabte', 'Diumenge'],

                   'y': consum , #Array de consum (extract from CSV).

                   'type': 'bar', # Tipus de DASH.

                   'name': 'SF'}
                ],
        'layout': {
                   'title': 'Consum diari'
                  }
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
