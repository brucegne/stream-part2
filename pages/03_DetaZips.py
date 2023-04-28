import streamlit as st
from deta import Deta
import json

# Connect to Deta Base with your Data Key
deta = Deta("b0fhjqxu_fG4y33DEMaK8qWfMGABUSbn8cGFNxXhC")
db = deta.Base("Zipcode")
"---"
"Here's everything stored in the database:"
"---"
county=st.text_input("Enter county")
state =st.text_input("Enter 2 character state")
goLook = st.button("Get Them")
if goLook: 
    qryString={}
    qryString["county?contains"] = county.title()
    qryString["state"] = state.upper()
    st.write(qryString)
    # db_content = db.fetch({'county?contains': 'Johnson', 'state': 'NE'}).items
    db_content = db.fetch(qryString).items
    st.dataframe(db_content)

