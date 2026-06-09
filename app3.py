import streamlit as st

# title
st.title("Student Dashboard")

# sidebar
st.sidebar.title("Selection")

city = st.sidebar.selectbox(
    "City",
    ["Adoni", "MDL", "Kurnool"]
)

# student inputs
name = st.text_input("Enter Name")

marks = st.number_input(
    "Marks",
    min_value=0,
    max_value=100,
    step=1
)

# submit button
submit = st.button("Submit")

# columns
col1, col2 = st.columns(2)

# run only after button click
if submit:

    # LEFT COLUMN
    with col1:

        st.subheader("Student Details")

        st.write("Name:", name)

        st.write("City:", city)

        st.write("Marks:", marks)

    # RIGHT COLUMN
    with col2:

        st.subheader("Result")

        # pass/fail
        if marks >= 35:

            st.success("Pass")

        else:

            st.error("Fail")

        # grading system
        if marks >= 90:

            st.write("Grade A")

        elif marks >= 75:

            st.write("Grade B")

        elif marks >= 50:

            st.write("Grade C")

        elif marks >= 35:

            st.write("Grade D")

        else:

            st.write("No Grade")
    

