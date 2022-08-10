from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash
import dash_table
import dash_daq as daq
import pandas as pd
import dash_table_experiments as dt
import base64
import os
from flask import send_from_directory
import dash_bootstrap_components as dbc
import home 
from app import app
from datetime import datetime
import weather

external_stylesheets = ['https://codepen.io/unicorndy/pen/GRJXrvP.css','https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']

#Insert your javascript here. In this example, addthis.com has been added to the web app for people to share their webpage
external_scripts = [{
                    'type': 'text/javascript', #depends on your application
                    'src': 'insert your addthis.com js here',
                    }]

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA], external_scripts = external_scripts)
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG],external_scripts = external_scripts)

app.title = 'Readable Password Generator'

#for heroku to run correctly
server = app.server

#Overwrite your CSS setting by including style locally
colors = {
    'background': '#2D2D2D',
    'text': '#7FDBFF',
    'figure_text': '#ffffff',
    'confirmed_text':'#3CA4FF',
    'deaths_text':'#f44336',
    'recovered_text':'#5A9E6F',
    'highest_case_bg':'#393939',
    
}

#Creating custom style for local use
divBorderStyle = {
    'backgroundColor' : '#393939',
    'borderRadius': '12px',
    'lineHeight': 0.9,
}

#Creating custom style for local use
boxBorderStyle = {
    'borderColor' : '#393939',
    'borderStyle': 'solid',
    'borderRadius': '10px',
    'borderWidth':2,
}

nav = dbc.Nav(
    [
                
    ],
    
)
PAGE_SIZE = 100 
app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(html.Div(
            [
                            html.Div(id='live-update-weather',
                            style={'font-size': '10px'}),
                            dcc.Interval(
                                    id='interval-component_weather',
                                    interval=30*60000, # in milliseconds
                                    n_intervals=0
                            )
                    ]
            ),align="start"),
            dbc.Col(html.Div(
                html.H3(
                            children='The Password Generator',
                            style={
                                'textAlign': 'center',
                                'color': colors['text']
                            }
                        )
                    ),align="center"),
            dbc.Col(html.Div(
                
                    [
                            html.Div(id='live-update-text',
                            style={'font-size': '10px'}),
                            dcc.Interval(
                                    id='interval-component',
                                    interval=1*1000, # in milliseconds
                                    n_intervals=0
                            )
                    ]),align="center")
        ],justify='center'
    
    ),
    dbc.Row(),

    dbc.Row(
        [
            dbc.Col(html.Div(nav))
        ],
    
    ),       
    html.Div([
    dcc.Location(id = 'url', refresh = True),
    html.Div(id = 'page-content'),
    #html.Div(dash_table.DataTable())
    ])


        
    
]
)
########### Callbacks ################
@app.callback(
    dash.dependencies.Output('toggle-switch-output', 'children'),
    [dash.dependencies.Input('my-toggle-switch', 'value')])
def update_output(value):
    if value:
        pass
    else:
        pass
@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_date(n):
      return [html.H4(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), 
                        style={
                                'textAlign': 'right',
                                'color': colors['text']
                            }
             )]   
@app.callback(Output('live-update-weather', 'children'),
              [Input('interval-component_weather', 'n_intervals')])
def update_weather(n):
    print('Calling weather')
    return [html.H4('Bangalore:'+str(weather.getWeather()), 
                        style={
                                'textAlign': 'left',
                                'color': colors['text']
                            }
             )]  
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    return home.layout()
if __name__ == '__main__':
    app.run_server(debug=False)