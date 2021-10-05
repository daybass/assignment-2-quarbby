# An Emotional 2020 US Elections

By Adya Danaditya and Lynnette Ng

andrew ids: adanadit and huixiann

## Introduction
The 2021 US Elections was held on November 2 2021. We visualize emotions related to the theme of voter fraud during the elections. 

### Goals of the project
This data visualization aims to help the users explore the following questions:
1. What is the general emotions and sentiment displayed in the tweets regarding voter fraud before and after the 2021 US Elections? 
2. Visualize and analyze Tweet volume, patterns, emotions and sentiments associated to keywords before and after the election. 

## Data
### Collection Methodology

The data was obtained from the IDeaS (Center for Informed Democracy and Social-Cybersecurity) lab at CMU, in Societal Computing program. The details of the data collection is described below. 

Data was collected using the Twitter V1 API. We collected data regarding voter fraud one week before and after the elections respectively using the Twitter hashtag streaming functionality. The timeframe for collections were (a) before election: October 27 to November 2 2021; (b) after election: November 3 to November 9 2021.

The list of hashtags used in the collection includes: #corruptelection, #deadvoters, #deceasedvoters, #dominionvotingsystems, #electionfraud, #electionintegrity, #fakeelection, #fakevotes, #fraudulentelection, #legalvotesonly, #legitimatevotesonly, #massivecorruption, #riggedelection, #stolenelection, #trumpismypresident, #voterfraud.

This dataset was annotated with emotions for each tweets. This was performed with the [PySentimento](https://github.com/pysentimiento/pysentimiento) emotion analyzer library, which is a machine learning model for annotating emotions. This annotates each tweet with one of the emotions: disgust, anger, fear, joy, sadness.
The dataset was also annotated with sentiments, which was done using the [Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) engine, which returns probabilities of positive and negative in the tweets. 

In total, we collected 417,830 tweets before the election and more than 4.35 million tweets after the election. 

In the next section we describe how we filtered the data so it is more manageable for interactive data visualization. We also describe further how we process the data to sieve out insights.

### Data Processing

After receiving the data, we performed data processing to clean the data in order to be able to better visualize it. 

After cleaning, we have around 30,000 tweets before the election.

For all tweets, we preprocessed it to remove the English stopwords. 

We processed sentiment to give an overall sentiment for each tweet, by adding the positive and negative sentiment with their respective signs. 

## Design Decisions
Initial mockup can be seen here:
https://docs.google.com/presentation/d/1gVf_JU8ncSO_rvnL-b4GniScFeKmmUdKV0SR8Q3bImw/edit#slide=id.gf1467485af_0_98

We wanted to begin with the keywords that people would search regarding voter fraud so we added a text search bar. 
With that, we displayed the volume of tweets related to that search. 
Then we wanted to showcase how the tweet information changed before and after the elections, so we divided the page into two, for before and after the elections.

## Deductions from the Data

## Limitations
There are several limitations of our data visualization. First and foremost, the Twitter V1 API only allows collection of 1% of the tweets, which means there are a lot of tweets that may not be collected. Second, the tweets collected are defined by hashtags that we curated, and we might have missed out some of them. Third, because of the browser limitations, we had to filter out some portions of the tweets, which means that some information may have been lost in the process. Nonetheless, we have xxx number of tweets, which should be sufficiently huge to deduce insights.

## Development Process
### Work Split
The work was split equally among the pair of team members. Adya did the data cleaning and overall design. Lynnette did the data collection and processing. Both contributed to the building of the interactive data science visualization.

### Time Spent
One week was spent collecting, processing and finalizing the dataset. Another week was spent wrangling with the Streamlit library.

### Aspects that took the most time
Two aspects took the most time: (a) data cleaning, in which we first did a manual inspection of the data, then performed exploratory data analysis to understand the distribution of the data and any duplicate and null values; (b) building the interaction in the visualization because we were not used to data visualization in Python.
