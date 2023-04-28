import streamlit as st
from deta import Deta
import json

# Connect to Deta Base with your Data Key
deta = Deta("b0fhjqxu_fG4y33DEMaK8qWfMGABUSbn8cGFNxXhC")
db = deta.Base("Zipcode")
hdr = st.container()
city = st.text_input("Enter city")
county = st.text_input("Or enter county")
state = st.text_input("Enter 2 character state")
goLook = st.button("Search")
if goLook:
    qryString={}
    if city.strip() == "":
        qryString["county?contains"] = county.title()
    else:
        qryString["city?contains"] = city.title()
    if state.strip() != "":
        qryString["state"] = state.upper()
    db_content = db.fetch(qryString).items

    st.dataframe(db_content)
    if len(db_content) > 0:
        hdr.write("Total locations found :"+str(len(db_content)))
        st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: red;'>Smaller headline in black </h2>", unsafe_allow_html=True)
    city = ""
    county = ""
    state = ""