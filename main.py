import streamlit as st
import gspread
import pandas as pd
import numpy as np
import requests, json
from time import sleep

st.set_page_config(page_title="Heartland Advantage - Home",
                    page_icon=":bar_chart:",
                    layout="wide")


work_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users.json'
user_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users/%s.json'

def makeKey():
    return('KEY'+str(time.time()).split('.')[1])

gc = gspread.service_account("secure.json")

sh = gc.open("WorkDataBook")
ws = sh.worksheet('System')
# ws.delete_rows(7)

st.write("Multi-row search results")
res = ws.findall('68516')
for rec in res:
    st.write(ws.row_values(rec.row))
    
# ws.delete_rows(7)
st.write("Multi-row search results")
res = ws.findall('68404')
for rec in res:
    st.write(ws.row_values(rec.row))
    
df = (ws.get_all_values())
st.write('Total data rows that exist',(len(df)-1))
for rec in df:
    if rec[1] != 'Name':
        st.write(rec)

