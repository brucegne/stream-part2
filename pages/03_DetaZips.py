import streamlit as st
import pandas as pd
from deta import Deta
import json

# Connect to Deta Base with your Data Key
deta = Deta("b0fhjqxu_fG4y33DEMaK8qWfMGABUSbn8cGFNxXhC")
db = deta.Base("Zipcode")
st.markdown("<h1 style='text-align: center; color: grey;'>Zipcode Lookup by County</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: red;'>Online for IA, NE, KS</h2>", unsafe_allow_html=True)
hdr = st.container()
qryString = {}
county = st.text_input("Enter partial county name and press enter.")
if county:
    qryString["county?contains"] = county.title()
    db_content = db.fetch(qryString).items
    try:
        df = pd.DataFrame(db_content)
        if len(df.filter(items=['city','county', 'state', 'population']).sort_values(by=['city','county']))>9:
            st.dataframe(df.filter(items=['city','county', 'state','zip', 'population']).sort_values(by=['city','county']))
            hdr.success("Total locations found :"+str(len(db_content)))
        else:
            hdr.info("No matches found." + str(qryString))
    except:
        st.error("Error processing query  " + str(qryString))
           