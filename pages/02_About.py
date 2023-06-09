import streamlit as st
import gspread
import pandas as pd
import numpy as np
import requests, json, time

def makeKey():
    return('KEY'+str(time.time()).split('.')[1])

gc = gspread.service_account("secure.json")

sh = gc.open("WorkDataBook")
ws = sh.worksheet('System')

st.set_page_config(page_title="Heartland Advantage Form Demo",
                    page_icon=":house:",
                    layout="wide")

work_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users.json'
user_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users/%s.json'

st.write(st.session_state)

st.header("About Us")

lcol, ccol, rcol = st.columns([1,3,1])
with ccol:
    form1 = st.form(key="header_form",clear_on_submit=True)
    user_first = form1.text_input("First Name", key="first")
    user_last = form1.text_input("Last Name", key="last")
    user_phone = form1.text_input("Telephone", key="phone")
    user_food = form1.multiselect('Buy', ['milk', 'apples', 'potatoes'], key="food")
    user_address = form1.text_input("Address", key="address")
    user_bio = form1.text_area("About Bio", key="bio")
    user_regdate = form1.date_input("Enter your DOB",key="dob")
    usr_submit = form1.form_submit_button("Send")
    if usr_submit:
        post_url = work_url
        post_data = {}
        post_data['name'] = user_first
        post_data['email'] = user_phone
        post_data['comments'] = user_bio
        res = requests.post(post_url,json=post_data)
        lcol.write("{0}, {1} is already to go".format(user_first, user_last))
        lcol.write(user_food)
        st.snow()
        st.session_state['blowhard'] = 'I did this.'
        kv = makeKey()
        new_row=[kv, user_first, user_last, user_phone, user_address, user_bio]
        ws.append_row(new_row)
        rcol.success(user_bio)
