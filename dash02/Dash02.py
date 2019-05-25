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


dia1 = sys.argv[1]

s = mycol.find_one( {'_id': dia1})
s2 = mycol.find_one( {'_id': dia1})

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


#Data 1


trace1 = go.Scatter(
    x=obj2,
    y=obj1,
    name=dia1
)


dia2 = sys.argv[2]

string1 = mycol.find_one( {'_id': dia2})
string2 = mycol.find_one( {'_id': dia2})

array1 = []
array2 = []


for c in string1['consum']:
    s2 = c['consum']
    array1.append(s2)

for c2 in string2['consum']:
    s3 = c2['diahora']
    array2.append(s3)


string1 = json.dumps(array1)

string2 = json.dumps(array2, default = myconverter)

objecte1 = json.loads(string1)
objecte2 = json.loads(string2)



#Data 2
# La X ha de ser la mateixa que la del trace anterior 
trace2 = go.Scatter(
    x=obj2,
    y=objecte1,
    name=dia2
)



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Comparativa entre 2 dates',
            style={
            'textAlign': 'center',
            }
            ),



dcc.Graph(
        id='example-graph',
        figure={
        'data': [trace1, trace2],
        'layout': {
                   'title': ''
                  }
                }
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
    





