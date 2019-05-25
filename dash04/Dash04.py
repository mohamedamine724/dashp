import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import csv
import pymongo
import json
import datetime
import sys
from dateutil.parser import *
import pprint
import json
import numpy as np
import math




### Mongo Connection ###
myclient = pymongo.MongoClient("mongodb://192.168.56.105:27017/")
mydb = myclient["projecte"]
mycol = mydb["consum"]


#Functions

def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper


start = sys.argv[1] #"2018-10-13" 

s = mycol.find_one( {'_id': start})
array_consum = []

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
 
    return sum/len(lista)


arr1 = []

for c in s['consum']:
    s = c['consum']
    arr1.append(s)

s = json.dumps(arr1)

obj1 = json.loads(s)
myarray = np.asarray(obj1)
final = np.split(myarray, 24)

# POR CADA ARRAY (P) CALCULAR EL PROMEDIO --> 
consum_per_horas = []
for p in final:
    promedio = promediarLista(p)
    promedio = truncate(promedio, 2)

    consum_per_horas.append(promedio) 
    






trace1 = go.Bar(
    x=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"],
    y=consum_per_horas,
    name="Hola"
)






external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Consum agrupat per hores',
            style={
            'textAlign': 'center',
            }
            ),



dcc.Graph(
        id='example-graph',
        figure={
        'data': [trace1],
        'layout': {
                   'title': 'Agrupació per hores'
                  }
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
    




