import streamlit as st
# creatin counter app
if count not in st.session_state:
    st.session_state.count=0
submit1=st.button("Increase")
if submit1:
    st.session_state.count=+1
submit2=st.button("Decrese")
if submit2:
    st.session_state.count=-1
st.write("Current counter value:",st.session_state.count) 
submit3=st.button("Reset")
if submit3:
    st.session_state.count=0   