import httpx
import asyncio
from fastapi import FastAPI, BackgroundTasks
from datetime import datetime, timedelta
from bs4 import BeautifulSoup 

#TODO
# calc elo function
#
#TODO
# update elo function 

elo_ratings = {}

async def fetch_game_data(date):
    # fetch game data function
    #

async def fetch_calc_historical_ratings():
    today = datetime.utcnow().date()
    current_year = today.year
