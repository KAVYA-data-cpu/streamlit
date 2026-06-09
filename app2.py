import streamlit as st
#Entering student details
name=st.text_input("Enter the name")
stupass=st.text_input("password",
                      type="password")
marks=st.number_input("Enter marks",
                   min_value=0,
                   max_value=100,
                   step=1)
st.button("Submit")
st.write("Name:",name)
st.write("Marks",marks)
#condition
if marks>=35:
    st.success("pass")
else:
    st.error("fail")
    
#grading system
    
if marks<=35:
    st.write("D grade")

elif marks<=50:
    st.write("C grade")
elif marks<=70:
    st.write("B grade")
elif marks<=100:
    st.write("A grade")

                      
                   

