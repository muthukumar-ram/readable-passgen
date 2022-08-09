import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_html_components as html
from hadoop.yarn import Yarn
import dash_bootstrap_components as dbc
from app import app
from dash import Dash
from dash import callback_context as ctx
import passgen



def layout():
    layout = html.Div([
    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
        
    dbc.Row([
                dbc.Col(),
                dbc.Col(html.Div([dbc.Button('Generate', className="btn-1",id='button',n_clicks=0),
                        ]),align="right"),
                dbc.Col()
            ],justify="right"),
    dbc.Row([dbc.Col(),dbc.Col(html.Div([html.Br(),html.Span(id="button-output", style={"verticalAlign": "middle"})])),dbc.Col()],justify="right"),
    
    ])
    
    return layout

@app.callback(
    Output('button-output', 'children'),
    [Input('button', 'n_clicks')])
def clicks(n_clicks):
    if n_clicks == 0 or n_clicks == None:
        return ''
    else:
        return passgen.genPass()