import streamlit as st
import pandas as pd
from deta import Deta

deta = Deta(st.secrets["data_key"])
db = deta.Base("basis")

topZone = st.empty()
topZone.title("Loading basis data")

detdat = db.fetch().items

df = pd.DataFrame(detdat)

st.dataframe(df.filter(items=['ent_date','commodity', 'buyer', 'location', 'basis']).sort_values(by=['commodity','buyer']))

st.table(df.filter(items=['ent_date','commodity', 'buyer', 'location', 'basis']).sort_values(by=['commodity','buyer']))

