import streamlit as st

st.set_page_config(page_title="Nifty Stuff",
                    page_icon=":house:",
                    layout="wide")

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
        lcol.write("{0}, {1} is already to go".format(user_first, user_last))
        lcol.write(user_food)
        rcol.success(user_bio)
