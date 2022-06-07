import streamlit as st
from app import prices_intervals, intro, select_date


# List of function that will create drop down menu

page_names_to_funcs = {
    "Intro": intro,
    "Intervals":prices_intervals,
    "Custom data range":select_date,
}

demo_name = st.sidebar.selectbox("Choose a section", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()