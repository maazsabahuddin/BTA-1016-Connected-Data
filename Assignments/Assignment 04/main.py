# Framework imports
from fastapi import FastAPI

# Python imports
import uvicorn
import requests
import json

app = FastAPI()


@app.get("/")
def read_root():
    return "Server running.."


@app.get("/player/{player_id}")
def get_player(player_id: int):
    """
    This function will return details of a specific player
    :param player_id:
    :return:
    """
    response = requests.get(f"https://www.balldontlie.io/api/v1/players/{player_id}")
    data = json.loads(response.text)
    response = {
        'data': data
    }
    return response


@app.get("/players")
def get_players():
    """
    This function will return all the players
    :return:
    """
    response = requests.get("https://www.balldontlie.io/api/v1/players")
    data = json.loads(response.text)['data']
    response = {
        'count': len(data),
        'data': data
    }
    return response


@app.get("/team/{team_id}")
def get_team(team_id: int):
    """
    This function will return details of a specific team
    :param team_id:
    :return:
    """
    response = requests.get(f"https://www.balldontlie.io/api/v1/teams/{team_id}")
    data = json.loads(response.text)
    response = {
        'data': data
    }
    return response


@app.get("/teams")
def get_teams():
    """
    This function will return all the teams
    :return:
    """
    response = requests.get("https://www.balldontlie.io/api/v1/teams")
    data = json.loads(response.text)['data']
    response = {
        'count': len(data),
        'data': data
    }
    return response


@app.get("/stats")
def get_stats():
    """
    This function will return all the stats
    :return:
    """
    response = requests.get("https://www.balldontlie.io/api/v1/stats")
    data = json.loads(response.text)['data']
    response = {
        'count': len(data),
        'data': data
    }
    return response


@app.get("/season/averages")
def get_season_averages(player_id: str):
    """
    This function will return player season average.
    :return:
    """
    response = requests.get(f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}")
    data = json.loads(response.text)['data'][0]
    response = {
        'data': data
    }
    return response


@app.get("/game/{game_id}")
def get_game(game_id: int):
    """
    This function will return details of a specific game_id
    :param game_id:
    :return:
    """
    response = requests.get(f"https://www.balldontlie.io/api/v1/games/{game_id}")
    data = json.loads(response.text)
    response = {
        'data': data
    }
    return response


@app.get("/games")
def get_games():
    """
    This function will return all the games
    :return:
    """
    response = requests.get("https://www.balldontlie.io/api/v1/games")
    data = json.loads(response.text)['data']
    response = {
        'count': len(data),
        'data': data
    }
    return response


uvicorn.run(app, host="0.0.0.0", port=5000, debug=True)
