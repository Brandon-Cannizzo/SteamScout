import streamlit as st
from utils import get_game_details, search_steam_game, get_results

# Use full page width
st.set_page_config(layout="wide")

st.title("Home")

st.header("Method 1", anchor=None)

st.write("**1245620** is Elden Ring")
search_input = st.text_input("Search app id:")

if search_input:
    # This block only runs after user types something and hits Enter
    game_info = get_game_details(search_input)
    st.write(f"Game: {game_info['name']}, Price: {game_info['price_overview']['final_formatted']}")

st.divider()

name_input = st.text_input("Search steam game by name!")

if name_input:
    # This block only runs after user types something and hits Enter
    # Example Usage
    results = get_results(name_input)
    st.write(results)



#if st.button("Show me the top 10 games on steam"):
    #st.write(get_game_details(1245620))