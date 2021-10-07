import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import numpy as np
from plotly.graph_objs import Pie, Figure
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import altair as alt
import re

st.set_page_config(page_title="Tweet Emotions - Election 2020", page_icon=None, layout='centered', initial_sidebar_state='expanded', menu_items=None)

st.title('Tweet Explorer')



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

with st.container():
    st.subheader('Start by filtering the tweets by keywords')
    st.markdown("Use this filter to narrow your analysis to tweets containing certain keywords.  \n"
    "*You can try 'Joe Biden', 'Trump', 'Michigan' or 'stopthesteal' to start*")
    user_input = st.text_input("Keyword Filter", "Joe Biden")

with st.sidebar:
    st.image("https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/flag-united-states_1f1fa-1f1f8.png", width=80)
    st.title('Tweet Emotions around Voter Fraud Allegations in 2020 Elections')
    st.write('The 2020 US Elections happened on November 2nd, 2020. There were calls on voter fraud and a rigged election. We investigate how the emotions changed on these topics before and after the elections by analyzing data on emotions and psychological values on Twitter a week before and a week after the elections.')
    st.write('Find full details of the dataset [here](https://github.com/IDSF21/assignment-2-quarbby).')
    st.write('*This interactive Dashboard is developed by  \n *'
    'Lynnette Ng and Adya Danaditya ')

    if(user_input):
        st.subheader('Keyword filter used: '+user_input)
        st.button('Change Keyword')
    else:
        st.subheader('Enter a keyword filter on the input')

before_keyword_mask = df_before_election['text'].str.contains(user_input)
before_time_filtered_data = df_before_election.loc[before_keyword_mask]

after_keyword_mask = df_after_election['text'].str.contains(user_input)
after_time_filtered_data = df_after_election.loc[after_keyword_mask]


total_df = before_time_filtered_data.append(after_time_filtered_data)
total = total_df[DATE_COLUMN].dt.date.value_counts()
total_count = len(total_df)
before_count = len(before_time_filtered_data)
after_count = len(after_time_filtered_data)

if(before_count > 0):
    delta_count = (after_count-before_count) / before_count
else:
    delta_count = 0

#Dataset statistics
if(user_input):
    st.subheader("Statistic of tweets talking about '*"+user_input+"*'")
else:
    st.subheader("Statistic of tweets for the whole dataset")

col1, col2, col3 = st.columns(3)
col1.metric("Total tweets", f"{total_count:,}")
col2.metric("Tweets before election", f"{before_count:,}")
col3.metric("Tweets after election", f"{after_count:,}", f"{delta_count:.2f}"+"x")

st.bar_chart(total)

#Sentiment
if(user_input):
    st.subheader("Sentiment of tweets talking about '*"+user_input+"*'")
else:
    st.subheader("Sentiment of tweets in the whole dataset")

conditions = [
    (total_df['liwc.posemo'] < total_df['liwc.negemo']),
    (total_df['liwc.posemo'] > total_df['liwc.negemo']),
    (total_df['liwc.posemo'] == total_df['liwc.negemo'])
    ]

# create a list of the values we want to assign for each condition
values = ['negative', 'positive', 'neutral']

# create a new column and use np.select to assign values to it using our lists as arguments
total_df['sentiment'] = np.select(conditions, values)
total_df['date'] = total_df[DATE_COLUMN].dt.date
sentiment_table = total_df.groupby(['date','sentiment']).count()['id'].reset_index()
c = alt.Chart(sentiment_table).mark_bar(size=20).encode(
    x='date',
    y=alt.Y('id', axis=alt.Axis(values=[0,0.5,1]), stack='normalize', title='number of tweets'),
    color=alt.Color(
        'sentiment',
        scale=alt.Scale(
            domain=['negative','neutral', 'positive'],
            range=['#de425b', '#ffe9af', '#488f31'])
        )
    ).configure_legend(
      orient='bottom'
    )

sentiment_table['id'] = sentiment_table['id'].astype('int64', copy=False)
st.write(c, use_container_width=True)

st.markdown("Average sentiment on tweets around *'" + user_input + "'* is ")

#Time Analysis

if(user_input):
    st.subheader("What time do people usually tweet about '*"+user_input+"*'")
else:
    st.subheader("Time distribution of dataset")

row1_1, row1_space2, row1_2, row1_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row1_1:
    st.markdown('<p style="background-color:lightblue;color:white;font-size:1rem;padding: 5px; border-radius: 0.4rem">Before Elections</p>', unsafe_allow_html=True)
with row1_2:
    st.markdown('<p style="background-color:pink;color:white;font-size:1rem;padding: 5px; border-radius: 0.4rem">After Elections</p>', unsafe_allow_html=True)


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

#Wordcloud

if(user_input):
    st.subheader("Topics/terms around tweets with '*"+user_input+"*'")
else:
    st.subheader("Top terms in the whole dataset")

stopwords = set(STOPWORDS)
stopwords.update(["https", "t", "co", "let", "will", "s", "use", "take", "used", "people", "said",
            "say", "wasnt", "go", "well", "thing", "amp", "put", "&", "even", "Yet", user_input])

# st.subheader('TO PRE PROCESS THE TEXT IN PYTHON')
us_mask = np.array(Image.open("us_map.PNG"))
us_color = np.array(Image.open("us.jpeg"))

row1_1, row1_space2, row1_2, row1_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row1_1:
    st.markdown('<p style="background-color:lightblue;color:white;font-size:1rem;padding: 5px; border-radius: 0.4rem">Before Elections</p>', unsafe_allow_html=True)
with row1_2:
    st.markdown('<p style="background-color:pink;color:white;font-size:1rem;padding: 5px; border-radius: 0.4rem">After Elections</p>', unsafe_allow_html=True)

row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (1, 0.1, 1, 0.1))

word_cleaning_before = ' '.join(text for text in before_time_filtered_data['text'])
word_cleaning_before = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",word_cleaning_before)
word_cleaning_before = word_cleaning_before.replace(user_input, '')

word_cleaning_after = ' '.join(text for text in after_time_filtered_data['text'])
word_cleaning_after = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",word_cleaning_after)
word_cleaning_after = word_cleaning_after.replace(user_input, '')

with row4_1:
    wordcloud_before = WordCloud(stopwords=stopwords, mask = us_mask, background_color="white", mode="RGB", max_words=100, width=800, height=400).generate(word_cleaning_before)
    fig, ax = plt.subplots(figsize=(5,5))
    image_colors = ImageColorGenerator(us_color)
    plt.tight_layout(pad=0)
    plt.imshow(wordcloud_before.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)

    st.write(list(wordcloud_before.words_.keys())[:20])

with row4_2:
    wordcloud_after = WordCloud(stopwords=stopwords, mask = us_mask, max_font_size=100, background_color="white", mode="RGB", max_words=100).generate(word_cleaning_after)
    image_colors = ImageColorGenerator(us_color)
    plt.tight_layout(pad=0)
    plt.imshow(wordcloud_after.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)

    st.write(list(wordcloud_after.words_.keys())[:20])

#Emotional Analysis

if(user_input):
    st.subheader("Topics/terms around tweets with '*"+user_input+"*'")
else:
    st.subheader("Top terms in the whole dataset")
row1_1, row1_space2, row1_2, row1_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row1_1:
    st.markdown('<p style="background-color:lightblue;color:white;font-size:1rem;padding: 5px; border-radius: 0.4rem">Before Elections</p>', unsafe_allow_html=True)
with row1_2:
    st.markdown('<p style="background-color:pink;color:white;font-size:1rem;padding: 5px; border-radius: 0.4rem">After Elections</p>', unsafe_allow_html=True)


row2_1, row2_space2, row2_2, row2_space3 = st.columns(
    (1, 0.1, 1, 0.1))
with row2_1:
    percent = before_time_filtered_data['highest_emotion'].value_counts(normalize=True).mul(100).round(2)
    _data = Pie(labels=percent.index.tolist(),values=percent.values.tolist(),hoverinfo='label+percent')
    fig = Figure(data=[_data])

    st.plotly_chart(fig,use_container_width=True)
with row2_2:
    percent2 = after_time_filtered_data['highest_emotion'].value_counts(normalize=True).mul(100).round(2)
    _data2 = Pie(labels=percent2.index.tolist(),values=percent2.values.tolist(),hoverinfo='label+percent')
    fig2 = Figure(data=[_data2])

    st.plotly_chart(fig2,use_container_width=True)

st.markdown("Most common tagged emotion on tweets around *'" + user_input + "'* is ")

a, space1, b, space2, c, space3, d, space4, e = st.columns(
    (0.5, 0.1, 0.5, 0.1, 0.5, 0.1, 0.5, 0.1, 0.5))

with a:
    st.markdown("Sample tweet tagged with 'Disgust' around *'" + user_input + "'*")

with b:
    st.markdown("Sample tweet tagged with 'Sadness' around *'" + user_input + "'*")

with c:
    st.markdown("Sample tweet tagged with 'Joy' around *'" + user_input + "'*")

with d:
    st.markdown("Sample tweet tagged with 'Anger' around *'" + user_input + "'*")

with e:
    st.markdown("Sample tweet tagged with 'Fear' around *'" + user_input + "'*")
