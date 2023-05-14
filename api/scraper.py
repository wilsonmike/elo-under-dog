import httpx
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.baseball-reference.com"

async def fetch_page(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text

async def get_team_stats(year):
    batting_url = f"{BASE_URL}/leagues/MLB/{year}-standard-batting.shtml"
    pitching_url = f"{BASE_URL}/leagues/MLB/{year}-standard-pitching.shtml"
    
    batting_page = await fetch_page(batting_url)
    pitching_page = await fetch_page(pitching_url)
    
    batting_soup = BeautifulSoup(batting_page, "html.parser")
    pitching_soup = 
