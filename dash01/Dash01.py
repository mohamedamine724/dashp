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


start = sys.argv[1]

s = mycol.find_one( {'_id': start})
s2 = mycol.find_one( {'_id': start})

arr1 = []
arr2 = []


for c in s['consum']:
    s = c['consum']
    arr1.append(s)

for c2 in s2['consum']:
    s2 = c2['diahora']
    arr2.append(s2)


s = json.dumps(arr1)

s2 = json.dumps(arr2, default = myconverter)

obj1 = json.loads(s)
obj2 = json.loads(s2)

array1 = obj2
array2 = obj1

trace1 = go.Scatter(
    x=array1,
    y=array2,
    name=start
)




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H3(children="Consum elèctric d'un dia (mostres cada 5 minuts)",
            style={
            'textAlign': 'center',
            }
            ),


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
    





