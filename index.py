import streamlit as st
import gspread
import pandas as pd
import numpy as np
import requests, json

st.set_page_config(page_title="Nifty Stuff",
                    page_icon=":bar_chart:",
                    layout="wide")


page_nav = st.sidebar.radio("Select Page",["Firebase","About Us"])
if page_nav == "Firebase":

    """
    # :camera:  :boat:  :wastebasket:
    """

    st.title("Welcome to StreamLit")

    work_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users.json'

    # requests.post(work_url, json={'name':'Gordon, Dana Marie', 'age': 8})

    results = requests.get(work_url)
    res = results.json()
    for rec in res:
        st.write(res[rec]['name'],res[rec]['comments'])

if page_nav == "About Us":
    st.title("Everything About What we do")

    st.write("Ain't this stuff neat")

