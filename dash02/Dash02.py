import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import csv
import pymongo
import json
import datetime
import sys

ejex=["2018-10-11 00:00:00", "2018-10-11 00:05:00", "2018-10-11 00:10:00", "2018-10-11 00:15:00", "2018-10-11 00:20:00", "2018-10-11 00:25:00", "2018-10-11 00:30:00", "2018-10-11 00:35:00", "2018-10-11 00:40:00", "2018-10-11 00:45:00", "2018-10-11 00:50:00", "2018-10-11 00:55:00", "2018-10-11 01:00:00", "2018-10-11 01:05:00", "2018-10-11 01:10:00", "2018-10-11 01:15:00", "2018-10-11 01:20:00", "2018-10-11 01:25:00", "2018-10-11 01:30:00", "2018-10-11 01:35:00", "2018-10-11 01:40:00", "2018-10-11 01:45:00", "2018-10-11 01:50:00", "2018-10-11 01:55:00", "2018-10-11 02:00:00", "2018-10-11 02:05:00", "2018-10-11 02:10:00", "2018-10-11 02:15:00", "2018-10-11 02:20:00", "2018-10-11 02:25:00", "2018-10-11 02:30:00", "2018-10-11 02:35:00", "2018-10-11 02:40:00", "2018-10-11 02:45:00", "2018-10-11 02:50:00", "2018-10-11 02:55:00", "2018-10-11 03:00:00", "2018-10-11 03:05:00", "2018-10-11 03:10:00", "2018-10-11 03:15:00", "2018-10-11 03:20:00", "2018-10-11 03:25:00", "2018-10-11 03:30:00", "2018-10-11 03:35:00", "2018-10-11 03:40:00", "2018-10-11 03:45:00", "2018-10-11 03:50:00", "2018-10-11 03:55:00", "2018-10-11 04:00:00", "2018-10-11 04:05:00", "2018-10-11 04:10:00", "2018-10-11 04:15:00", "2018-10-11 04:20:00", "2018-10-11 04:25:00", "2018-10-11 04:30:00", "2018-10-11 04:35:00", "2018-10-11 04:40:00", "2018-10-11 04:45:00", "2018-10-11 04:50:00", "2018-10-11 04:55:00", "2018-10-11 05:00:00", "2018-10-11 05:05:00", "2018-10-11 05:10:00", "2018-10-11 05:15:00", "2018-10-11 05:20:00", "2018-10-11 05:25:00", "2018-10-11 05:30:00", "2018-10-11 05:35:00", "2018-10-11 05:40:00", "2018-10-11 05:45:00", "2018-10-11 05:50:00", "2018-10-11 05:55:00", "2018-10-11 06:00:00", "2018-10-11 06:05:00", "2018-10-11 06:10:00", "2018-10-11 06:15:00", "2018-10-11 06:20:00", "2018-10-11 06:25:00", "2018-10-11 06:30:00", "2018-10-11 06:35:00", "2018-10-11 06:40:00", "2018-10-11 06:45:00", "2018-10-11 06:50:00", "2018-10-11 06:55:00", "2018-10-11 07:00:00", "2018-10-11 07:05:00", "2018-10-11 07:10:00", "2018-10-11 07:15:00", "2018-10-11 07:20:00", "2018-10-11 07:25:00", "2018-10-11 07:30:00", "2018-10-11 07:35:00", "2018-10-11 07:40:00", "2018-10-11 07:45:00", "2018-10-11 07:50:00", "2018-10-11 07:55:00", "2018-10-11 08:00:00", "2018-10-11 08:05:00", "2018-10-11 08:10:00", "2018-10-11 08:15:00", "2018-10-11 08:20:00", "2018-10-11 08:25:00", "2018-10-11 08:30:00", "2018-10-11 08:35:00", "2018-10-11 08:40:00", "2018-10-11 08:45:00", "2018-10-11 08:50:00", "2018-10-11 08:55:00", "2018-10-11 09:00:00", "2018-10-11 09:05:00", "2018-10-11 09:10:00", "2018-10-11 09:15:00", "2018-10-11 09:20:00", "2018-10-11 09:25:00", "2018-10-11 09:30:00", "2018-10-11 09:35:00", "2018-10-11 09:40:00", "2018-10-11 09:45:00", "2018-10-11 09:50:00", "2018-10-11 09:55:00", "2018-10-11 10:00:00", "2018-10-11 10:05:00", "2018-10-11 10:10:00", "2018-10-11 10:15:00", "2018-10-11 10:20:00", "2018-10-11 10:25:00", "2018-10-11 10:30:00", "2018-10-11 10:35:00", "2018-10-11 10:40:00", "2018-10-11 10:45:00", "2018-10-11 10:50:00", "2018-10-11 10:55:00", "2018-10-11 11:00:00", "2018-10-11 11:05:00", "2018-10-11 11:10:00", "2018-10-11 11:15:00", "2018-10-11 11:20:00", "2018-10-11 11:25:00", "2018-10-11 11:30:00", "2018-10-11 11:35:00", "2018-10-11 11:40:00", "2018-10-11 11:45:00", "2018-10-11 11:50:00", "2018-10-11 11:55:00", "2018-10-11 12:00:00", "2018-10-11 12:05:00", "2018-10-11 12:10:00", "2018-10-11 12:15:00", "2018-10-11 12:20:00", "2018-10-11 12:25:00", "2018-10-11 12:30:00", "2018-10-11 12:35:00", "2018-10-11 12:40:00", "2018-10-11 12:45:00", "2018-10-11 12:50:00", "2018-10-11 12:55:00", "2018-10-11 13:00:00", "2018-10-11 13:05:00", "2018-10-11 13:10:00", "2018-10-11 13:15:00", "2018-10-11 13:20:00", "2018-10-11 13:25:00", "2018-10-11 13:30:00", "2018-10-11 13:35:00", "2018-10-11 13:40:00", "2018-10-11 13:45:00", "2018-10-11 13:50:00", "2018-10-11 13:55:00", "2018-10-11 14:00:00", "2018-10-11 14:05:00", "2018-10-11 14:10:00", "2018-10-11 14:15:00", "2018-10-11 14:20:00", "2018-10-11 14:25:00", "2018-10-11 14:30:00", "2018-10-11 14:35:00", "2018-10-11 14:40:00", "2018-10-11 14:45:00", "2018-10-11 14:50:00", "2018-10-11 14:55:00", "2018-10-11 15:00:00", "2018-10-11 15:05:00", "2018-10-11 15:10:00", "2018-10-11 15:15:00", "2018-10-11 15:20:00", "2018-10-11 15:25:00", "2018-10-11 15:30:00", "2018-10-11 15:35:00", "2018-10-11 15:40:00", "2018-10-11 15:45:00", "2018-10-11 15:50:00", "2018-10-11 15:55:00", "2018-10-11 16:00:00", "2018-10-11 16:05:00", "2018-10-11 16:10:00", "2018-10-11 16:15:00", "2018-10-11 16:20:00", "2018-10-11 16:25:00", "2018-10-11 16:30:00", "2018-10-11 16:35:00", "2018-10-11 16:40:00", "2018-10-11 16:45:00", "2018-10-11 16:50:00", "2018-10-11 16:55:00", "2018-10-11 17:00:00", "2018-10-11 17:05:00", "2018-10-11 17:10:00", "2018-10-11 17:15:00", "2018-10-11 17:20:00", "2018-10-11 17:25:00", "2018-10-11 17:30:00", "2018-10-11 17:35:00", "2018-10-11 17:40:00", "2018-10-11 17:45:00", "2018-10-11 17:50:00", "2018-10-11 17:55:00", "2018-10-11 18:00:00", "2018-10-11 18:05:00", "2018-10-11 18:10:00", "2018-10-11 18:15:00", "2018-10-11 18:20:00", "2018-10-11 18:25:00", "2018-10-11 18:30:00", "2018-10-11 18:35:00", "2018-10-11 18:40:00", "2018-10-11 18:45:00", "2018-10-11 18:50:00", "2018-10-11 18:55:00", "2018-10-11 19:00:00", "2018-10-11 19:05:00", "2018-10-11 19:10:00", "2018-10-11 19:15:00", "2018-10-11 19:20:00", "2018-10-11 19:25:00", "2018-10-11 19:30:00", "2018-10-11 19:35:00", "2018-10-11 19:40:00", "2018-10-11 19:45:00", "2018-10-11 19:50:00", "2018-10-11 19:55:00", "2018-10-11 20:00:00", "2018-10-11 20:05:00", "2018-10-11 20:10:00", "2018-10-11 20:15:00", "2018-10-11 20:20:00", "2018-10-11 20:25:00", "2018-10-11 20:30:00", "2018-10-11 20:35:00", "2018-10-11 20:40:00", "2018-10-11 20:45:00", "2018-10-11 20:50:00", "2018-10-11 20:55:00", "2018-10-11 21:00:00", "2018-10-11 21:05:00", "2018-10-11 21:10:00", "2018-10-11 21:15:00", "2018-10-11 21:20:00", "2018-10-11 21:25:00", "2018-10-11 21:30:00", "2018-10-11 21:35:00", "2018-10-11 21:40:00", "2018-10-11 21:45:00", "2018-10-11 21:50:00", "2018-10-11 21:55:00", "2018-10-11 22:00:00", "2018-10-11 22:05:00", "2018-10-11 22:10:00", "2018-10-11 22:15:00", "2018-10-11 22:20:00", "2018-10-11 22:25:00", "2018-10-11 22:30:00", "2018-10-11 22:35:00", "2018-10-11 22:40:00", "2018-10-11 22:45:00", "2018-10-11 22:50:00", "2018-10-11 22:55:00", "2018-10-11 23:00:00", "2018-10-11 23:05:00", "2018-10-11 23:10:00", "2018-10-11 23:15:00", "2018-10-11 23:20:00", "2018-10-11 23:25:00", "2018-10-11 23:30:00", "2018-10-11 23:35:00", "2018-10-11 23:40:00", "2018-10-11 23:45:00", "2018-10-11 23:50:00", "2018-10-11 23:55:00"],
## COMPARAR DIAS SIN LA FECHA (SOLAPADOS)

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
# La X tiene que ser la misma que la de arriba.
trace2 = go.Scatter(
    x=obj2,
    y=objecte1,
    name=dia2
)



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Consum Elèctric'),
    html.Div(children='''Dashboard: Per controlar el consum diari.'''),



dcc.Graph(
        id='example-graph',
        figure={
        'data': [trace1, trace2],
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
