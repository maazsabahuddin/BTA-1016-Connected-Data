# Python imports
import datetime
import requests
import json

# Framework imports
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


app = Dash("app")

url = "https://Assignment-04.maazsabahuddin.repl.co"


def get_data(endpoint=""):
    """
    This function will return the count of number of teams
    :return:
    """
    response = requests.get(f"{url}/{endpoint}")
    data = json.loads(response.text)
    return data


colors = {
    'background': '#000000',
    'text': '#ffffff'
}

players = get_data(endpoint="players")
teams = get_data(endpoint="teams")
top_10_teams_data = [[team['name'], team['full_name'], team['division'], team['conference'], team['city'],
                      team['abbreviation']] for team in teams['data'][1:11]]
top_10_teams_data.insert(0, ["Name", "Full Name", "Division", "Conference", "City", "Abbreviation"])

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'
fig_table = go.Figure(data=[go.Table(
  header=dict(
    values=[],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left', 'center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=top_10_teams_data,
    line_color='darkslategray',
    fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]*5],
    align=['left', 'center'],
    font=dict(color='darkslategray', size=11)
    ))
])

df = pd.DataFrame({
    "Height": [int(player['height_feet'])*12 + int(player['height_inches'])
               for player in players['data'] if player.get('height_feet')],
    "Weight": [int(player['weight_pounds']) for player in players['data'] if player.get('height_feet')],
})

fig = px.bar(df, x="Height", y="Weight", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig_table.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('cryingjordan.jpeg'),
                     id='jordan-image',
                     style={
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
            )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Basket Ball", style={"margin-bottom": "0px", 'color': 'white'}),
                html.H5("Basket Ball Game Statistics Dashboard", style={"margin-top": "0px", 'color': 'white'}),
                html.P("Incorporated 5 different calls for visualizing the data on this dashboard",
                       style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H6('Date Time: ' + str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M")),
                    style={'color': 'orange'}),
        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        html.Div([
            html.Div([
                html.H5("Number of Teams / Player and Games played till now.",
                        style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column"),

    ], className="row flex-display", style={"margin-bottom": "10px", "margin-top": "10px"}),

    html.Div([
        html.Div([
            html.H6(children='Teams',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P(f"{get_data(endpoint='teams')['count']}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40
                   }),
            ],
            className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Players',
                    style={
                        'textAlign': 'center',
                        'color': 'white'
                    }),

            html.P(f"{players['count']}",
                   style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 40}
                   ),
            ],
            className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Games',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{get_data(endpoint='games')['count']}",
                   style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 40}
                   ),
            ],
            className="card_container three columns",
        ),

    ], className="row flex-display"),

    html.Div([
        html.Div([
            html.Div([
                html.H5("Players Weight in Pound and their Height in Inches Comparison",
                        style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column"),

    ], className="row flex-display", style={"margin-bottom": "10px", "margin-top": "10px"}),

    dcc.Graph(
        id='players-data-graph',
        figure=fig
    ),

    html.Div([
        html.Div([
            html.Div([
                html.H5("Teams Data Table", style={"margin-top": "0px", 'color': 'white'}),
                html.P(f"Around {teams['count']} teams participated in the basketball game and some of them are "
                       f"listed below in the plotly datatable.", style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="teams_table_header"),

    ], className="row flex-display", style={"margin-bottom": "10px", "margin-top": "10px"}),

    dcc.Graph(
        id='teams_table',
        figure=fig_table
    )

])

app.run_server(host='0.0.0.0', port=8000, debug=True)
