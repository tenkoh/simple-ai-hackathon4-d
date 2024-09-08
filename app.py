import streamlit as st

st.title("Simple Streamlit App")
st.write("Enter your text below:")

user_input = st.text_input("Input something:")
if user_input:
    st.write(f"You entered: {user_input}")
