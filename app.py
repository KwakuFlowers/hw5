import os
import string
from urllib import response
from dotenv import find_dotenv, load_dotenv
import requests
import json

load_dotenv(find_dotenv())

api_search = "https://api.themoviedb.org/3/trending/movie/week"

API_KEY = os.getenv("API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}"}

res = requests.get(api_search, headers=headers)
actual_res = res.json()
for n in range(10):
    title_name = actual_res["results"][n]["title"]
    print(title_name)
