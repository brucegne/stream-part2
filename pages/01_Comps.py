import streamlit as st
import streamlit.components.v1 as components
import os, json, time
from PIL import Image

st.write(st.session_state)

def save_uploadedfile(uploadedfile):
     with open(os.path.join("static",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to /static".format(uploadedfile.name))

image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    st.write(file_details)
    save_uploadedfile(image_file)

path = "./static"
img_list = []
obj = os.scandir(path)
for entry in obj:
    img_list.append(entry.name)

img = st.sidebar.selectbox("Choose Image", img_list)
if img:
    st.write(img)

st.markdown(
        f'<img src="./app/static/{img}" height="333" style="border: 5px solid orange">',
        unsafe_allow_html=True,
    )