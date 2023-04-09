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
	with st.sidebar:
		form =  st.form(key='edit_form',clear_on_submit=True)
		uname = st.selectbox("Choose User", rlist)
		if "Please"  not in uname:
		    user_rec = requests.get(user_url % (klist[uname]))
		    uemail = user_rec.json()['email']
		    ucomments = user_rec.json()['comments']
		    user_name = form.text_input('User Name', value=uname)
		    user_email = form.text_input('User Email', value=uemail)
		    user_comments = form.text_input('Comments', value=ucomments)
		    usr_submit = form.form_submit_button(label="Save Changes")
		    st.sidebar.write(" ")
		    st.sidebar.write(" ")
		    if usr_submit:
		      post_url = user_url % klist[uname]
		      post_data = {}
		      post_data['name'] = user_name
		      post_data['email'] = user_email
		      post_data['comments'] = user_comments
		      res = requests.patch(post_url,json=post_data)
              
	
if page_nav == "About Us":
	st.title("Everything About What we do")

	st.write("Ain't this stuff neat")

	tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

	with tab1:
	   st.header("A cat")
	   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

	with tab2:
	   st.header("A dog")
	   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

	with tab3:
	   st.header("An owl")
	   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

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
