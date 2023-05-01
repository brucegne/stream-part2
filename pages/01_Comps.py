import streamlit as st
import streamlit.components.v1 as components
import os, json, time
from deta import Deta, Drive
from PIL import Image

project = Deta(st.secrets["data_key"])
drive_name = 'PicCollection'
drive = project.Drive(drive_name)

topEnd = st.empty()

picList = drive.list()
photoList = []
for rec in picList['names']:
    photoList.append(rec)
selPhoto = st.selectbox("Choose Photo", photoList)
if selPhoto:
    img = drive.get(selPhoto)
    pic = img.read()
    topEnd.image(pic,width=150)
    img.close()

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file")

# If user attempts to upload a file.
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    # Show the image filename and image.
#    st.write(f'filename: {uploaded_file.name}')
#    st.image(bytes_data)

    # Upload the image to deta using put with filename and data.
    drive.put(uploaded_file.name, data=bytes_data)

