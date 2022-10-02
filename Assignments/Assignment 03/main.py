# Maaz Sabah Uddin
# A00257491

from flask import Flask, render_template, request
import random
import plotly
import plotly.express as px
import pandas as pd
import json

app = Flask('app')
players = {"bob": "https://robohash.org/bob.png", "joe": "https://robohash.org/joe.png",
           "moe": "https://robohash.org/moe.png", "sue": "https://robohash.org/sue.png"}


@app.route("/match")
def match1():
    players_score = {"bob": random.randint(1, 100), "joe": random.randint(1, 100),
                     "moe": random.randint(1, 100), "sue": random.randint(1, 100)}
    final_teams = {"team_a": "", "team_b": ""}

    if players_score["bob"] > players_score["joe"]:
        first_match = "Bob Won the game!"
        final_teams.update({"team_a": "Bob"})
    elif players_score["bob"] == players_score["joe"]:
        first_match = "Match tie!"
        final_teams.update({"team_a": "Tie"})
    else:
        first_match = "Joe Won the game!"
        final_teams.update({"team_a": "Joe"})

    if players_score["moe"] > players_score["sue"]:
        second_match = "Moe Won the game!"
        final_teams.update({"team_b": "Moe"})
    elif players_score["moe"] == players_score["sue"]:
        second_match = "Match tie!"
        final_teams.update({"team_b": "Tie"})
    else:
        second_match = "Sue Won the game!"
        final_teams.update({"team_b": "Sue"})

    final_teams_score = {"team_a": random.randint(1, 100), "team_b": random.randint(1, 100)}
    if final_teams_score['team_a'] > final_teams_score['team_b']:
        final_match = f"{final_teams['team_a']} Won the game!"
    elif final_teams_score['team_a'] == final_teams_score['team_b']:
        final_match = "Match tie!"
    else:
        final_match = f"{final_teams['team_b']} Won the game!"

    return render_template("index.html",
                           players=players,
                           players_score=players_score,
                           bob_joe_match=first_match,
                           moe_sue_match=second_match,
                           final_teams=final_teams,
                           final_match=final_match,
                           final_teams_score=final_teams_score,
                           show_results=True)


@app.route('/')
def index_page():
    """
    This is the index page of the web.
    :return:
    """
    return render_template("index.html",
                           players=players,
                           players_score={"bob": 0, "joe": 0,
                                          "moe": 0, "sue": 0},
                           bob_joe_match="",
                           moe_sue_match="",
                           show_results=False)


@app.route('/graph', methods=['GET'])
def visualize():
    """
    This end-point will construct a graph
    :return:
    """
    score = {"names": [request.args.get(f"name{i}") for i in range(1, 5)],
             "numbers": [int(request.args.get(f"number{i}")) for i in range(1, 5)]}
    df = pd.DataFrame(score)
    fig = px.bar(df, x='names', y='numbers')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('graph.html', graphJSON=graphJSON)


app.run(host='0.0.0.0', port=5000, debug=True)
