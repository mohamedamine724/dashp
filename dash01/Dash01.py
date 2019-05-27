import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import csv
import pymongo
import json
import datetime
import sys


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

### Mongo Connection ###
myclient = pymongo.MongoClient("mongodb://192.168.56.105:27017/")
mydb = myclient["projecte"]
mycol = mydb["consum"]

#Agafo la data introduïda des del PHP
start = sys.argv[1]

#Realitzo el find al Mongo per obtenir tant la array del consum com de la data/hora
s = mycol.find_one( {'_id': start})
s2 = mycol.find_one( {'_id': start})

arr1 = []
arr2 = []

#Array consum
for c in s['consum']:
    s = c['consum']
    arr1.append(s)
#Array diahora
for c2 in s2['consum']:
    s2 = c2['diahora']
    arr2.append(s2)

#Conversió de la arr1 a tipus JSON Array.
s = json.dumps(arr1)

#Conversió de la arr2 a tipus JSON Array, fent server la funció myconverter per transformar els camps en datetime.
s2 = json.dumps(arr2, default = myconverter)

#Carrego la array JSON a les variables obj1/obj2 amb les seves respectives dades.
obj1 = json.loads(s)
obj2 = json.loads(s2)

array1 = obj2
array2 = obj1

#Creació del Trace (linia del gràfic), passant-li les arrays anteriors.
trace1 = go.Scatter(
    x=array1,
    y=array2,
    name=start
)




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Creació del object / clase app --> Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Afegim un layout (html) a la app (al dash)
app.layout = html.Div(children=[
    html.H3(children="Consum elèctric d'un dia (mostres cada 5 minuts)",
            style={
            'textAlign': 'center',
            }
            ),

#Creació del gràfic passant-li el trace1.
dcc.Graph(
        id='example-graph',
        figure={
        'data': [trace1],
        'layout': {
                   'title': 'Consum diari ('+start+')',
                  },
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
    





