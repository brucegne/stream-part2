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

page_nav = st.sidebar.radio("Select Page",["Add User","Edit User", "Firebase","About Us", "Images"])

if page_nav == "Add User":

	st.header("GSpread Contact Entry Form")
	st.caption("Check under 'Firebase' to see all entries")
	form =  st.form(key='editform1234',clear_on_submit=True)
	user_name = form.text_input('User Name', value='')
	user_email = form.text_input('User Email', value='')
	user_comments = form.text_area('Comments', value='')
	usr_submit = form.form_submit_button(label="Save Changes")
	if usr_submit:
	    post_url = work_url
	    post_data = {}
	    post_data['name'] = user_name
	    post_data['email'] = user_email
	    post_data['comments'] = user_comments
#	    res = requests.post(post_url,json=post_data)
	    page_nav = "Firebase"

	

if page_nav == "Firebase":

	st.title("Welcome to StreamLit")
# requests.post(work_url, json={'name':'Gordon, Dana Marie', 'age': 8})

	rlist=['Please Select']
	klist={}
	results = requests.get(work_url)
	res = results.json()
	for rec in res:
		rlist.append(res[rec]['name'])
		klist[res[rec]['name']]=rec
		st.write(rec,'____',res[rec]['name'],res[rec]['comments'])
              
	
if page_nav == "About Us":
	st.title("Everything About who we are and What we do")

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
