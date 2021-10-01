import streamlit as st
import pandas as pd
import numpy as np
from plotly.graph_objs import Pie, Figure
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
from plotly import graph_objs as go

st.set_page_config(layout="wide")

row0_1, row0_spacer2 = st.columns(
    (3.2, 0.3))
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

st.markdown('<p style=color:black;font-size:30px;font-weight:bold;">Go ahead and filter the Tweets by keywords</p>', unsafe_allow_html=True)
user_input = st.text_input("Keyword Filter", "Joe Biden")

before_keyword_mask = df_before_election['text'].str.contains(user_input)
before_time_filtered_data = df_before_election.loc[before_keyword_mask]

after_keyword_mask = df_after_election['text'].str.contains(user_input)
after_time_filtered_data = df_after_election.loc[after_keyword_mask]

total_df = before_time_filtered_data.append(after_time_filtered_data)
st.markdown('<p><span style=color:red;font-size:30px;font-weight:bold;>' + str(len(total_df)) + '<span>' + 
            '<span style=color:black;font-size:30px;font-weight:bold;> Tweets are talking about </span>' + 
            '<span style=color:red;font-size:30px;font-weight:bold;>' + user_input + '</span></p>', unsafe_allow_html=True)
total = total_df[DATE_COLUMN].dt.date.value_counts()
st.bar_chart(total)

st.markdown('<p><span style=color:black;font-size:30px;font-weight:bold;> Sentiment of tweets about </span>' + 
            '<span style=color:red;font-size:30px;font-weight:bold;>' + user_input + '</span></p>', unsafe_allow_html=True)

total_posneg_df = total_df.groupby([total_df[DATE_COLUMN].dt.date])["posneg"].mean()*100
total_posneg_df = total_posneg_df.reset_index()
st.line_chart(total_posneg_df.rename(columns={DATE_COLUMN:'index', 'posneg': 'sentiment'}).set_index('index'))

st.markdown('<p><span style=color:black;font-size:24px;font-weight:bold;>Average Sentiment about </span>' + 
            '<span style=color:red;font-size:24px;font-weight:bold;>' + user_input + 
            '</span><span style=color:black;font-size:24px;font-weight:bold;> is POSITIVE<span></p>', unsafe_allow_html=True)

row1_1, row1_space2, row1_2, row1_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row1_1:
    st.markdown('<p style="background-color:lightblue;color:black;font-size:32px;font-weight:bold;">Before Elections</p>', unsafe_allow_html=True)
with row1_2:
    st.markdown('<p style="background-color:pink;color:black;font-size:32px;font-weight:bold;">After Elections</p>', unsafe_allow_html=True)

st.markdown('<p><span style=color:black;font-size:30px;font-weight:bold;font-weight:bold;>What time do people usually tweet about </span>' + 
            '<span style=color:red;font-size:30px;font-weight:bold;font-weight:bold;>' + user_input + '</span><span style=color:black;font-size:30px;font-weight:bold;font-weight:bold;>?</b></p>', unsafe_allow_html=True)

row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (1, 0.1, 1, 0.1))

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

st.markdown('<p><span style=color:black;font-size:30px;font-weight:bold;font-weight:bold;>What are the topics of the tweets surrounding </span>' + 
            '<span style=color:red;font-size:30px;font-weight:bold;font-weight:bold;>' + user_input + '</span><span style=color:black;font-size:30px;font-weight:bold;font-weight:bold;>?</b></p>', unsafe_allow_html=True)
stopwords = set(STOPWORDS)
stopwords.update(["https", "t", "co", "let", "will", "s", "use", "take", "used", "people", "said", 
            "say", "wasnt", "go", "well", "thing", "amp", "put", "&", "even", "Yet"])
# st.subheader('TO PRE PROCESS THE TEXT IN PYTHON')
mask = np.array(Image.open("us.PNG"))

row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (1, 0.1, 1, 0.1))

with row4_1:
    before_text_string = ' '.join(text for text in before_time_filtered_data['text'])
    wordcloud_before = WordCloud(stopwords=stopwords, background_color="white", mode="RGB", max_words=1000, mask=mask, width=800, height=400).generate(before_text_string)
    image_colors = ImageColorGenerator(mask)
    fig, ax = plt.subplots(figsize=(5,5))
    plt.tight_layout(pad=0)
    plt.imshow(wordcloud_before.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)

with row4_2:
    after_text_string = ' '.join(text for text in after_time_filtered_data['text'])
    wordcloud_after = WordCloud(stopwords=stopwords, max_font_size=100, background_color="white", mode="RGB", max_words=1000, mask=mask).generate(after_text_string)
    image_colors = ImageColorGenerator(mask)
    fig, ax = plt.subplots()
    plt.imshow(wordcloud_after.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)

st.markdown('<p><span style=color:black;font-size:24px;font-weight:bold;>The most popular words surrounding </span>' + 
            '<span style=color:red;font-size:24px;font-weight:bold;>' + user_input + 
            '</span><span style=color:black;font-size:24px;font-weight:bold;> is<span></p>', unsafe_allow_html=True)

st.markdown('<p><span style=color:black;font-size:30px;font-weight:bold;font-weight:bold;>What are the emotions of the tweets surrounding </span>' + 
            '<span style=color:red;font-size:30px;font-weight:bold;font-weight:bold;>' + user_input + '</span><span style=color:black;font-size:30px;font-weight:bold;font-weight:bold;>?</b></p>', unsafe_allow_html=True)

row2_1, row2_space2, row2_2, row2_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row2_1:
    percent = before_time_filtered_data['highest_emotion'].value_counts(normalize=True).mul(100).round(2)
    _data = Pie(labels=percent.index.tolist(),values=percent.values.tolist(),hoverinfo='label+percent')
    fig = Figure(data=[_data])

    st.write(fig)
with row2_2:
    percent2 = after_time_filtered_data['highest_emotion'].value_counts(normalize=True).mul(100).round(2)
    _data2 = Pie(labels=percent2.index.tolist(),values=percent2.values.tolist(),hoverinfo='label+percent')
    fig2 = Figure(data=[_data2])

    st.write(fig2)

st.markdown('<p><span style=color:black;font-size:24px;font-weight:bold;>The most popular emotion surrounding </span>' + 
            '<span style=color:red;font-size:24px;font-weight:bold;>' + user_input + 
            '</span><span style=color:black;font-size:24px;font-weight:bold;> is<span></p>', unsafe_allow_html=True)