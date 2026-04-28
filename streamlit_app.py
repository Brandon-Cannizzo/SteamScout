import streamlit as st


home_page = st.Page("1_home_page.py", title="Home")
pg = st.navigation([home_page], position="top")
pg.run()