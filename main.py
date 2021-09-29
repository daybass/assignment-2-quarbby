import streamlit as st
import pandas as pd
import numpy as np
import json
import seaborn as sns
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import RendererAgg

st.set_page_config(layout="wide")
matplotlib.use("agg")
_lock = RendererAgg.lock

row0_spacer1, row0_1, row0_spacer2 = st.columns(
    (.1, 3.2, .1))
row0_1.title('An Emotional 2021 US Elections')

row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))
row1_1.subheader('The US Elections happened on .... ')

@st.cache
def load_data():
    DATE_COLUMN = 'created_at'
    random_sample_rows = 10000

    # TODO: FIGURE OUT HOW TO READ FROM AN ONLINE RESOURCE 
    #  
    # df_before_election = pd.read_json('https://drive.google.com/file/d/1sIRjjkmrPxSCDoK2HA7Q9woXZDLQhRJ9/view?usp=sharing', lines=True)
    # df_after_elections = pd.read_json('https://drive.google.com/file/d/1KB_k0qNba1rIZzI7WH5CAGSJY0wmYXLQ/view?usp=sharing', lines=True)

    df_before_election = pd.read_json(r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_after_election_11_03_through_11_09_processed.json', lines=True)
    df_after_elections = pd.read_json(r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_before_election_10_27_through_11_02_processed.json', lines=True)

    df_before_election = df_before_election.sample(n=random_sample_rows)
    df_after_elections = df_after_elections.sample(n=random_sample_rows)

    df_before_election[DATE_COLUMN] = pd.to_datetime(df_before_election[DATE_COLUMN])
    df_after_elections[DATE_COLUMN] = pd.to_datetime(df_before_election[DATE_COLUMN])

    df_before_election = df_before_election.fillna(0)
    df_after_elections = df_after_elections.fillna(0)

    return df_before_election, df_after_elections

df_before_election, df_after_elections = load_data()

line1_spacer1, line1_1, line1_spacer2 = st.columns((.1, 3.2, .1))
st.header('First we look at the number of tweets over time before and after the US Elections')
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (.1, 1, .1, 1, .1))

with row3_1, _lock:
    st.subheader('Before Elections')

with row3_2, _lock:
    st.subheader('After Elections')

line2_spacer1, line2_1, line2_spacer2 = st.columns((.1, 3.2, .1))
st.header('Then let\'s look at the emotions [we can do emotion flow graph, or change in emotions]')

line3_spacer1, line3_1, line3_spacer2 = st.columns((.1, 3.2, .1))
st.header('Now we look at the feeling of time [liwc focuspast, focuspresent, focusfuture]')

line4_spacer1, line4_1, line4_spacer2 = st.columns((.1, 3.2, .1))
st.header('Now we look at the social processes [liwc family, friend, female male]')

line5_spacer1, line5_1, line5_spacer2 = st.columns((.1, 3.2, .1))
st.header('Now we look at the drives [liwc affliation, achieve, power, reward, risk]')

line6_spacer1, line6_1, line6_spacer2 = st.columns((.1, 3.2, .1))
st.header('Now we look at the moral values')

line7_spacer1, line7_1, line7_spacer2 = st.columns((.1, 3.2, .1))
st.header('Okay so we do some regressions')

line8_spacer1, line8_1, line8_spacer2 = st.columns((.1, 3.2, .1))
st.header('And have some conclusions')