
import pandas as pd
import dash
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
data = px.data.gapminder()

# print(data.head())

app = dash.Dash()

# app.layout = html.H1(children='Hands on Dash',style={'color':'red','text-align':'center'})

app.layout = html.Div([
    html.Div(children=[html.H1("DashBoard",style={'color':'red','text-align':'center','margin-bottom':'4px'})],style={'border':'1px solid black','float':'left','width':'100%','height':'50px'}),
    html.Div(children=[dcc.Graph(id='scatter-plot',
                                 figure={'data':[go.Scatter(x=data['pop'],
                                                             y=data['gdpPercap'],
                                                             mode='markers' )],
                                         'layout':go.Layout(title='Scatter Plot')})],
style={'border':'1px solid black','float':'left','width':'49%','height':'350px'}),

    html.Div(
children=[dcc.Graph(id='box-plot',
                                 figure={ 'data':[go.Box(x=data['gdpPercap'])],
                                         'layout':go.Layout(title='Box Plot')})],
        style={'border':'1px solid black','float':'left','width':'49%','height':'350px'})
])


app.run_server(debug=True)



