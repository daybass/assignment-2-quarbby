import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.offline as py
from plotly.graph_objs import Pie, Layout,Figure

st.set_page_config(layout="wide")
sns.set()

row0_spacer1, row0_1, row0_spacer2 = st.columns(
    (0.1, 3.2, 0.3))
with row0_1:
    st.markdown("![US Flag gif](https://media.giphy.com/media/3osxYcwi3hCVbzNYqY/giphy.gif)")
    row0_1.title('An Emotional 2021 US Elections')

st.subheader('The US Elections happened on 2 November 2021. There were calls on voter fraud and a rigged election. We investigate how the emotions changed on these topics before and after the elections by analyzing data on emotions and psychological values on Twitter a week before and a week after the elections.')
st.write('Find full details of the data [here](https://github.com/IDSF21/assignment-2-quarbby).')

DATE_COLUMN = 'created_at'

@st.cache
def load_data():
    df_before_election = pd.read_csv('./data/before_cleaned_emotion.csv')
    df_after_election = pd.read_csv('./data/after_cleaned_emotion.csv')

    df_before_election[DATE_COLUMN] = df_before_election[DATE_COLUMN].apply(lambda x: x.replace('+00:00', ''))
    df_before_election[DATE_COLUMN] = pd.to_datetime(df_before_election[DATE_COLUMN])
    df_after_election[DATE_COLUMN] = df_after_election[DATE_COLUMN].apply(lambda x: x.replace('+00:00', ''))
    df_after_election[DATE_COLUMN] = pd.to_datetime(df_after_election[DATE_COLUMN])

    df_before_election = df_before_election.fillna(0)
    df_after_election = df_after_election.fillna(0)

    return df_before_election, df_after_election

df_before_election, df_after_election = load_data()

user_input = st.text_input("Filter the data with keywords", "Joe Biden")

with st.sidebar:
    st.markdown(user_input)

before_keyword_mask = df_before_election['text'].str.contains(user_input)
before_time_filtered_data = df_before_election.loc[before_keyword_mask]

after_keyword_mask = df_after_election['text'].str.contains(user_input)
after_time_filtered_data = df_after_election.loc[after_keyword_mask]

total = before_time_filtered_data.append(after_time_filtered_data)

st.subheader('Number of Tweets over Time')
total = total[DATE_COLUMN].dt.date.value_counts()
st.bar_chart(total)
# st.write(total)

row1_1, row1_space2, row1_2, row1_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row1_1:
    st.markdown('<p style="background-color:lightblue;color:black;font-size:32px;">Before Elections<h2></p>', unsafe_allow_html=True)
with row1_2:
    st.markdown('<p style="background-color:pink;color:black;font-size:32px;">After Elections<h2></p>', unsafe_allow_html=True)

row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1))

with row3_1:
    st.text('By Hour of Day')
    hist_values_before = np.histogram(before_time_filtered_data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values_before)

    st.text('By Day of Week')
    hist_values_day_before = np.histogram(before_time_filtered_data[DATE_COLUMN].dt.day, bins=7, range=(0,7))[0]
    st.bar_chart(hist_values_day_before)

with row3_2:
    st.text('By Hour of Day')
    hist_values_after = np.histogram(after_time_filtered_data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values_after)

    st.text('By Day of Week')
    hist_values_day_after = np.histogram(after_time_filtered_data[DATE_COLUMN].dt.day, bins=7, range=(0,7))[0]
    st.bar_chart(hist_values_day_after)

st.header('First emotions')

row2_1, row2_space2, row2_2, row2_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row2_1:
    percent = before_time_filtered_data['highest_emotion'].value_counts(normalize=True).mul(100).round(2)
    _data = Pie(labels=percent.index.tolist(),values=percent.values.tolist(),hoverinfo='label+percent')
    fig = Figure(data=[_data])

    st.write(fig)
with row2_2:
    percent2 = after_time_filtered_data['highest_emotion'].value_counts(normalize=True).mul(100).round(2)
    _data2 = Pie(labels=percent.index.tolist(),values=percent.values.tolist(),hoverinfo='label+percent')
    fig2 = Figure(data=[_data])

    st.write(fig2)