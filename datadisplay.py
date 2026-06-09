import pandas as pd
import streamlit as st
df=pd.DataFrame({
    "crop":["rice","cotton","maize"],
    "confidence":[95,90,88]
    })
st.table(df)
st.dataframe(df)
    
