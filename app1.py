
import streamlit as st

st.write("Student Details:-")

# creating form container
with st.form("Student_Form"):

    # creating name input
    name = st.text_input("Enter the Name")

    # for age
    age = st.number_input("Enter the Age")

    # for city
    city = st.selectbox(
        "City",
        ["Adoni", "Kurnool", "MDL"]
    )

    # for gender
    gender = st.radio(
        "Gender",
        ["Male", "Female"]
    )

    # special form submit button
    ak = st.form_submit_button("Submit")

# checking submit
if ak:

    st.write("Name:", name)

    st.write("Age:", age)

    st.write("City:", city)

    st.write("Gender:", gender)
