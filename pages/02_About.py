import streamlit as st

st.set_page_config(page_title="Nifty Stuff",
                    page_icon=":house:",
                    layout="wide")

st.header("About Us")

lcol, ccol, rcol = st.columns([3,2,1])
ccol.write("Center")
rcol.write("Right")
with lcol:
    st.write("Lefty")
    form1 = st.form(key="header_form",clear_on_submit=True)
    user_first = form1.text_input("First Name")
    user_last = form1.text_input("Last Name")
    user_phone = form1.text_input("Telephone")
    user_food = form1.multiselect('Buy', ['milk', 'apples', 'potatoes'])
    user_address = form1.text_input("Address")
    user_bio = form1.text_area("About Bio")
    user_regdate = form1.date_input("Enter your DOB")
    usr_submit = form1.form_submit_button("Send")
    if usr_submit:
        ccol.write("{0}, {1} is already to go".format(user_first, user_last))
        ccol.write(user_food)
        lcol.success(user_bio)
