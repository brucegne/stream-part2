import streamlit as st
import pandas as pd
from deta import Deta
import time

# Data to be written to Deta Base

hdr = st.empty()

deta = Deta(st.secrets["data_key"])
db = deta.Base("bgfamily")

with st.form("form", clear_on_submit=True):
    name = st.text_input("Your name")
    age = st.text_input("Your age")
    notes = st.text_area("Enter the notes for this person")
    submitted = st.form_submit_button("Store in database")
    if submitted:
        db.put({"name": name, "age": age, "notes": notes})
        hdr.success(name+" Has been added to the database")
detdat = db.fetch().items
df = pd.DataFrame(detdat)
st.dataframe(df.filter(items=['name','age', 'notes', 'basis']).sort_values(by=['name','age']))

time.sleep(5)
hdr.write("")
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
# for rec in db_content:
#     st.write(rec['key'], str(rec['age']), rec['name'])
