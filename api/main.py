from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CSV_FILE = os.path.join(DATA_DIR, 'mlb_elo.csv')

def calculate_elo(home_elo, away_elo, home_score, away_score, k=20):
    home_expected = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
    away_expected = 1 / (1 + 10 ** ((home_elo - away_elo) / 400))

    if home_score > away_score:
        home_actual = 1
        away_actual = 0 
    elif home_score < away_score:
        home_actual = 0
        away_actual = 1
    else:
        home_actual = 0.5
        away_actual = 0.5

    new_home_elo = home_elo + k * (home_actual - home_expected)
    new_away_elo = away_elo + k * (home_actual - home_expected)

    return new_home_elo, new_away_elo

@app.get("/api/elo")
async def get_elo_ratings():
   df = pd.read_csv(CSV_FILE) 
   teams = df['team'].unique()
   ratings = {team: 1500 for team in teams}

   for index, row in df.iterrows():
       home_team, away_team = row['team'], row['opp']
       home_score, away_score = row['score'], row['opp_score']
       home_elo, away_elo = ratins[home_team], ratings[away_team]
       new_home_elo, new_away_elo = calculate_elo(home_elo, away_elo,
               home_score, away_score)   
       ratings[home_team] = new_home_elo
       ratings[away_team] = new_away_elo

    return [{"team": team, "rating": rating} for team, rating in
            ratings.items()]


       













