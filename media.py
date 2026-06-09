import streamlit as st
st.title("Crop Disease Detector")
uploaded_file=st.file_uploader(
    "choose file",
    type=["png","jpeg","jpg"]
    )
if uploaded_file is not None:
    st.image(uploaded_file)
    st.success("Image uploaded")
