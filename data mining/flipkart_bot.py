import requests 
from bs4 import BeautifulSoup
import os
import pandas as pd 
import datetime

def get_soup(url):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text)
    return None


