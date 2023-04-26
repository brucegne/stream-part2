import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json

# [server]
# enableStaticServing = true
# db = firestore.Client.from_service_account_json(".streamlit/fire-key.json")

key_dict = json.loads(st.secrets['textkey'])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

# Streamlit widgets to let a user create a new post
form = st.form(key="Form1",clear_on_submit=True)
title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")

# Once the user has submitted, upload it to the database
if title and url and submit:
	doc_ref = db.collection("posts").document(title)
	doc_ref.set({
		"title": title,
		"url": url
	})

# And then render each post, using some light Markdown
posts_ref = db.collection("posts")
for doc in posts_ref.stream():
	post = doc.to_dict()
	title = post["title"]
	url = post["url"]

	st.subheader(f"Post: {title}")
	st.write(f":link: [{url}]({url})")

emps_ref = db.collection("employee")
for doc in emps_ref.stream():
	post = doc.to_dict()
	age = post['age']
	lname = post['lname']
	name = post['name']
	st.write(f"{age}, {name}, {lname}")