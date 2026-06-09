import streamlit as st
import random
st.title("OTP login page")
name=st.text_input("Enter the name")
if "otp" not in st.session_state:
    st.session_state.otp=random.randint(100000,999999)
st.write("yoyr otp:",st.session_state.otp)
enterd_otp=st.number_input("Enter otp",step=1)
submit=st.button("Login")
if submit:
    if st.session_state.otp==enterd_otp:
        st.success("OTP Correct")
        st.success("Login successful")
    else:
        st.error("Check otp once again")

    