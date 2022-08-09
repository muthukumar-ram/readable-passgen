import dash
import os
import dash_html_components as html
from flask_caching import Cache
import dash_bootstrap_components as dbc


#app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],suppress_callback_exceptions=True)
server=app.server