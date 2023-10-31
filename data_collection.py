import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.write("# Welcome to Data Workshop! 👋")

    st.markdown("""During this workshop, you'll make experience of solvd data journey.""")

    text_input = st.text_input("Enter your name")
    job_input = st.text_input("What is your job?")
    number_input = st.text_input("How many years are you working for your company?")

    st.markdown(
        f"""
        My name is {text_input} \n
        I have been working as {job_input} \n
        at Solvd for {number_input} years
        """)

if __name__ == "__main__":
    run()
