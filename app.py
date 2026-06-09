import streamlit as st
name=st.text_input("Enter name")
kav=st.button("submit")
if kav:
    st.write("Hello",name)
    





