import streamlit as st
import time
st.title("Crop Prediction Stimulator")
predict=st.button("Predict crop")
if predict:
    with st.spinner("Predicting....."):
        time.sleep(3)
    bar=st.progress(0)
    for i in range (101):
        time.sleep(0.05)
    bar.progress(i)
    st.success("Recommended crop : Rice")


    
