import streamlit as st
st.title("Crop Recommendation Report Generator")
crop=st.text_input("Enter the crop")
predict=st.button("Generate Report")
if predict:
    st.download_button(
        "Download Report",
        crop,
        "crop.txt"
        )
