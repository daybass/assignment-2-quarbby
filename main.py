import streamlit as st
import pandas as pd
import numpy as np
import json
import seaborn as sns
import matplotlib
from matplotlib.figure import Figure

st.set_page_config(layout="wide")

row0_spacer1, row0_1, row0_spacer2 = st.columns(
    (.1, 3.2, .1))
row0_1.title('Emotions before/after the US Elections')

row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))
row1_1.subheader('short description')

@st.cache
def load_data():
    df_before_election = pd.read_json('https://drive.google.com/file/d/1sIRjjkmrPxSCDoK2HA7Q9woXZDLQhRJ9/view?usp=sharing', lines=True)
    df_after_elections = pd.read_json('https://drive.google.com/file/d/1KB_k0qNba1rIZzI7WH5CAGSJY0wmYXLQ/view?usp=sharing', lines=True)