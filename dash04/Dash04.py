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

x=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"],

## COMPARAR DIAS SIN LA FECHA (SOLAPADOS)



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

###data = json.load(s)
##pprint.pprint(s)
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
##    print(promedio)
    consum_per_horas.append(promedio) #Si multiplicamos por 0.12€ sabemos el gasto de dinero por hora.
    



##print(obj1[210])

##print(len(obj1))






    
##    print(s)
##
##for e in A:
##    print(e)

y = [22, 18, 16, 11, 12, 12, 11, 12, 14, 19, 18, 21, 15, 12, 13, 18, 19, 16, 18, 71, 54, 15, 17, 19]



##print ("Promedio = " + str(promediarLista(A)))
    


##print(json.dumps(array_consum, default = myconverter))
    
##dt = s['consum'][0]['consum']



##print(dt)

##mycol.delete_one({'_id': start})






trace1 = go.Bar(
    x=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"],
    y=consum_per_horas,
    name="Hola"
)






external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Consum Elèctric'),
    html.Div(children='''Dashum diari.'''),



dcc.Graph(
        id='example-graph',
        figure={
        'data': [trace1],
        'layout': {
                   'title': 'Consum diari'
                  }
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
    





##import plotly.plotly as py
##import plotly.graph_objs as go
##
##trace1 = go.Bar(
##    x=['giraffes', 'orangutans', 'monkeys'],
##    y=[20, 14, 23],
##    name='SF Zoo'
##)
##trace2 = go.Bar(
##    x=['giraffes', 'orangutans', 'monkeys'],
##    y=[12, 18, 29],
##    name='LA Zoo'
##)
##
##data = [trace1, trace2]
##layout = go.Layout(
##    barmode='group'
##)
##
##fig = go.Figure(data=data, layoutx=layout)
##py.iplot(fig, filename='grouped-bar')

