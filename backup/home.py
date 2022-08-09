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
    dbc.Row(),
    dbc.Row(),
    dbc.Row(),
    dbc.Row(),
    dbc.Row(),
    dbc.Row(),
        
    dbc.Row([
                dbc.Col(),
                dbc.Col(html.Div([html.Button('Generate', id='button'),
                        html.H3(id='button-clicks')]),align="right"),
                dbc.Col()
            ],justify="right"),
    dbc.Row(),
    
    ])
    
    return layout

@app.callback(
    Output('button-clicks', 'children'),
    [Input('button', 'n_clicks')])
def clicks(n_clicks):
    if n_clicks == None:
        return ''
    else:
        return passgen.genPass()