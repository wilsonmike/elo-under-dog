from fastapi import FastAPI
# TODO
# from mlb import mlb_teams, calculate_mlb_elo

app = FastAPI()

teams = [
    {"id": 1, "name": "New York Yankees", "elo": 1500},
    {"id": 2, "name": "Boston Red Sox", "elo": 1400},
    {"id": 3, "name": "Chicago Cubs", "elo": 1300},
]

@app.get("/api/teams")
async def get_teams():
    return teams

# TODO 
# api endpoints per league
# @app.get("/api/mlb")
#async def get_mlb_teams():
#    return mlb_teams
