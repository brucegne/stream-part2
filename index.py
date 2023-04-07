import streamlit as st
import gspread
import pandas as pd
import numpy as np
import requests, json

st.set_page_config(page_title="Nifty Stuff",
                    page_icon=":bar_chart:",
                    layout="wide")


page_nav = st.sidebar.radio("Select Page",["Firebase","About Us", "Images"])
if page_nav == "Firebase":

    """
    # :camera:  :boat:  :wastebasket:
    """

    st.title("Welcome to StreamLit")

    work_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users.json'
    user_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users/%s.json'

    # requests.post(work_url, json={'name':'Gordon, Dana Marie', 'age': 8})

    rlist=['Please Select']
    klist={}
    results = requests.get(work_url)
    res = results.json()
    for rec in res:
        rlist.append(res[rec]['name'])
        klist[res[rec]['name']]=rec
        st.write(res[rec]['name'],res[rec]['comments'])
    uname = st.sidebar.selectbox("Choose User", rlist)
    if "Please"  not in uname:
      user_rec = requests.get(user_url % (klist[uname]))
      uemail = user_rec.json()['email']
      ucomments = user_rec.json()['comments']
      with st.form(key='edit_form'):
        with st.sidebar:
            user_name = st.sidebar.text_input('User Name', value=uname)
            user_email = st.sidebar.text_input('User Email', value=uemail)
            user_comments = st.sidebar.text_input('Comments', value=ucomments)
            usr_submit = st.form_submit_button(label="Save Changes")
            if usr_submit:
              post_url = user_url % klist[uname]
              post_data = {}
              post_data['name'] = user_name
              post_data['email'] = user_email
              post_data['comments'] = user_comments
              res = requests.patch(post_url,json=post_data)
              st.sidebar.write("Form was processed")
        
if page_nav == "About Us":
    st.title("Everything About What we do")

    st.write("Ain't this stuff neat")

if page_nav == "Images":

  col1, col2, col3 = st.columns([1,2,1])

  with col1:
      col1.header("This is on the left")
      col1.subheader("This would be a little smaller")

  with col2:
      col2.header("This should be in the center")
      my_upload = st.file_uploader("Upload a local photo")
      my_image = st.camera_input("Take your picture", disabled=False)

  with col3:
      col3.header("This is hanging out on the right")
      if my_image:
          st.success("You got the picture")
          st.image(my_image)
      if my_upload:
          st.image(my_upload)
