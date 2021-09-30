import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
sns.set()

row0_spacer1, row0_1, row0_spacer2 = st.columns(
    (0.1, 3.2, 0.3))
with row0_1:
    st.markdown("![US Flag gif](https://media.giphy.com/media/3osxYcwi3hCVbzNYqY/giphy.gif)")
    row0_1.title('An Emotional 2021 US Elections')

st.subheader('The US Elections happened on 2 November 2021. There were calls on voter fraud and a rigged election. We investigate how the emotions changed on these topics before and after the elections by analyzing data on emotions and psychological values on Twitter a week before and a week after the elections.')
DATE_COLUMN = 'created_at'

@st.cache
def load_data():
    df_before_election = pd.read_csv('./data/before_cleaned.csv')
    df_after_election = pd.read_csv('./data/after_cleaned.csv')

    # df_before_election = pd.read_json(r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_after_election_11_03_through_11_09_processed.json', lines=True)
    # df_after_elections = pd.read_json(r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_before_election_10_27_through_11_02_processed.json', lines=True)

    df_before_election[DATE_COLUMN] = df_before_election[DATE_COLUMN].apply(lambda x: x.replace('+00:00', ''))
    df_before_election[DATE_COLUMN] = pd.to_datetime(df_before_election[DATE_COLUMN])
    df_after_election[DATE_COLUMN] = df_after_election[DATE_COLUMN].apply(lambda x: x.replace('+00:00', ''))
    df_after_election[DATE_COLUMN] = pd.to_datetime(df_after_election[DATE_COLUMN])

    df_before_election = df_before_election.fillna(0)
    df_after_election = df_after_election.fillna(0)

    return df_before_election, df_after_election

df_before_election, df_after_election = load_data()

st.header('First we look at the number of tweets over time before and after the US Elections')

min_date = min(df_before_election[DATE_COLUMN]).date()
max_date = max(df_after_election[DATE_COLUMN]).date()
date_format = 'YYYY-MM-DD HH:mm:ss'

st.write(min_date, max_date)

date_filter = st.slider('Select date range', min_value=min_date, max_value=max_date, value=(min_date, max_date), format=date_format)

with st.sidebar:
    st.markdown('🇺🇸 An Emotional US Elections')
    st.write('date range: ', date_filter)

before_mask = (df_before_election[DATE_COLUMN].dt.date >= date_filter[0]) & (df_before_election[DATE_COLUMN].dt.date <= date_filter[1])
before_time_filtered_data = df_before_election.loc[before_mask]

after_mask = (df_after_election[DATE_COLUMN].dt.date >= date_filter[0]) & (df_after_election[DATE_COLUMN].dt.date <= date_filter[1])
after_time_filtered_data = df_after_election.loc[after_mask]

before_time_filtered_data[DATE_COLUMN] = pd.to_datetime(before_time_filtered_data[DATE_COLUMN])
after_time_filtered_data[DATE_COLUMN] = pd.to_datetime(after_time_filtered_data[DATE_COLUMN])

row1_space1, row1_1, row1_space2, row1_2, row1_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1))
with row1_1:
    st.subheader('Before Elections')
with row1_2:
    st.subheader('After Elections')

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

st.header('Then let\'s look at the emotions [we can do emotion flow graph, or change in emotions]')

row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (.1, 1, .1, 1, .1))

st.write('We should add interactivity to choose emotion and put it to the sidebar')
emotion_columns = ["emotion.joy", "emotion.anger", "emotion.sadness", "emotion.disgust", "emotion.fear"]
emotion_columns_rename_dict = {"emotion.joy": "joy", "emotion.anger": "anger", "emotion.sadness": "sadness", 
                                                "emotion.disgust": "disgust", "emotion.fear": "fear"}

with row4_1:
    fig, ax = plt.subplots()
    emotion_df = before_time_filtered_data[emotion_columns]
    emotion_df = emotion_df.rename(columns= emotion_columns_rename_dict)
    emotion_mean = emotion_df.mean()
    st.bar_chart(emotion_mean)
    
st.header('Now we look at the feeling of time')
st.subheader('They are represented by the values of *past, present, future* which are inferred through the Tweets.')

row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns(
    (.1, 1, .1, 1, .1))

st.header('Now we look at the social processes [liwc family, friend, female male]')

st.header('Now we look at the drives [liwc affliation, achieve, power, reward, risk]')

st.header('Now we look at the moral values')

st.header('Okay so we do some regressions')

st.header('And have some conclusions')

st.subheader('Finally, if you want the full details of the psycholinguistic stuff we used, please refer [here](https://github.com/IDSF21/assignment-2-quarbby).')