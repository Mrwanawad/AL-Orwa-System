import os
import pandas as pd
import streamlit as st;                              st.set_page_config( 'Main Page', ':bar_chart:', 'wide' )
from streamlit_lottie import st_lottie
import json

st.markdown(
    """
    <style>
    /* Sidebar right border */
    [data-testid="stSidebar"] {
        border-right: 4px solid #0F52BA;  /* sapphire color */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
        .st-emotion-cache-8gkzs6 p {
            font-size: 25px !important;
        }
    </style>
""", unsafe_allow_html=True)
# streamlit run app/main.py

anim = json.load(open("app/lottie-anims/Financial Graph Loader.json"))

with st.sidebar :  st_lottie( anim, height=300, speed=3, loop=True, width= 150 )

st.markdown(  '<h1 style = "font-family:times new roman; font-size:95px;text-align:center;margin-top:-80px" ><i>AL ORWA Stock Tracking</i></h1>',unsafe_allow_html=True)
