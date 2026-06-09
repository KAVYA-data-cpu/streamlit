import streamlit as st
import pandas as pd
@st.cache_data()
def loading_dataset():
    df=pd.read_csv("C://Users//Admin//OneDrive//Book3.csv")
    return df
st.write(loading_dataset())
