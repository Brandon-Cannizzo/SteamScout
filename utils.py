import requests
from requests.exceptions import RequestException
import streamlit as st

# Uses the steam storefront api, allowing for searching directly
def get_game_details(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Data is keyed by the app_id
        return data[str(app_id)]['data']
    return None


def search_steam_game(game_name):
    # Public store search endpoint (no API key needed)
    search_url = "https://steampowered.com"
    
    params = {
        'term': game_name,
        'l': 'english',
        'cc': 'US'  # Country code (sets currency/availability)
    }
    
    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get('total') > 0:
            return data['items']
        else:
            return []
            
    except Exception as e:
        print(f"Error: {e}")
        return []


# https://gist.github.com/GermainZ/1a992ab4192adbe80280

STORE_URL = 'http://store.steampowered.com/app/{}/'
STOREFRONT_API_URL = 'http://store.steampowered.com/api/storesearch/?term={}&l=english&cc=US'


def get_results(text):
    query = text

    try:
        response = requests.get(STOREFRONT_API_URL.format(query))
    except RequestException:
        return None
    if not response:
        return None
    results = response.json() # Store list based on search
    if not results['items']:
        return 'No results found for "{}".'.format(query)
    # I can create a dictionary of top X results... maybe
    st.write(len(results))
    game = results['items'][0]
    name = game['name']
    if not 'price' in game:
        price = 'Free!'
    else:
        price = '${}'.format(game['price']['final'] / 100)
        discount = int((game['price']['initial'] - game['price']['final']) /
                       game['price']['initial'] * 100)
        if discount:
            price = '{} [-{}%]'.format(price, discount)
    platforms = []
    for platform, supported in game['platforms'].items():
        if supported:
            platforms.append(platform.capitalize())
    platforms = ', '.join(platforms)
    url = STORE_URL.format(game['id'])
    output = '{} -- {} ({}) <{}>'.format(name, price, platforms, url)

    return output