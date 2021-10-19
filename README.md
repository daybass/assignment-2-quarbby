# An Emotional 2020 US Elections
By Adya Danaditya and Lynnette Ng
Andrew IDs: adanadit and huixiann

## Introduction
The 2020 US Elections was held on November 2 2020. We visualize emotions related to the theme of voter fraud during the elections. 

### Goals of the project
This data visualization aims to help the users explore the following questions:
1. What is the general emotions and sentiment displayed in the tweets regarding voter fraud before and after the 2020 US Elections? 
2. Visualize and analyze Tweet volume, patterns, emotions and sentiments associated to keywords before and after the election. 

## Data
### Collection Methodology
The data was obtained from the IDeaS (Center for Informed Democracy and Social-Cybersecurity) lab at CMU, in Societal Computing program. The details of the data collection is described below. 

Data was collected using the Twitter V1 API. We collected data regarding voter fraud one week before and after the elections respectively using the Twitter hashtag streaming functionality. The timeframe for collections were (a) before election: October 27 to November 2 2020; (b) after election: November 3 to November 9 2020.

The list of hashtags used in the collection includes: #corruptelection, #deadvoters, #deceasedvoters, #dominionvotingsystems, #electionfraud, #electionintegrity, #fakeelection, #fakevotes, #fraudulentelection, #legalvotesonly, #legitimatevotesonly, #massivecorruption, #riggedelection, #stolenelection, #trumpismypresident, #voterfraud.

This dataset was annotated with emotions for each tweets. This was performed with the [PySentimento](https://github.com/pysentimiento/pysentimiento) emotion analyzer library, which is a machine learning model for annotating emotions. This annotates each tweet with one of the emotions: disgust, anger, fear, joy, sadness.
The dataset was also annotated with sentiments, which was done using the [Linguistic Inquiry and Word Count](https://liwc.wpengine.com/) engine, which returns probabilities of positive and negative in the tweets. 

In total, we collected 417,830 tweets before the election and more than 4.35 million tweets after the election. 

In the next section we describe how we filtered the data so it is more manageable for interactive data visualization. We also describe further how we process the data to sieve out insights.

### Data Processing

After receiving the data, we performed data processing to clean the data in order to be able to better visualize it as well as for the practical reason of making the interactive process run in a quick manner. The cleaning includes taking out tweets in the dataset which has missing values in its emotion and sentiment parameters and taking out tweets that are retweets of other tweets. 
After cleaning, we have around 30,000 tweets before the election and around 350,000 after the election.
The sentiment and emotion are predefined measures we got from the dataset.
We also created new columns tagging the prevailing sentiment and emotion of the tweet by processing sentiment and emotion measures of each tweet in the dataset and take the emotion or sentiment which is highest in value as the tag.

## Design Decisions and Expected Outcome
Initial mockup can be seen here:
https://docs.google.com/presentation/d/1gVf_JU8ncSO_rvnL-b4GniScFeKmmUdKV0SR8Q3bImw/edit#slide=id.gf1467485af_0_98
- NOTE that there are some ideas in the mockup that we left unimplemented, or some new ideas not put in the mockup due to implementability issues.
 
The main interactivity offered by this project is that the user can change the filtering keyword so they can get a sense of the context, emotion and sentiment surrounding that keyword before and after the election. 
Through keyword input we provided:
- The statistics of tweets in our database related to that search. This is achieved by histograms and multiple metric views.
- The context related to that keyword. This is achieved by word clouds, and ranking
- The emotional and sentiment value surrounding that keyword, shown by combinations of bar charts and pie charts
- A contrast from before and after the election by dividing the page into two, is for the user to discern the change of emotion before and after the elections.
- An further interactivity if the user want to see an exact sample of tweets in certain context or certain emotion, to get a deeper sense of the emotions at play.

## Limitations
There are several limitations of our data visualization. First and foremost, the Twitter V1 API only allows collection of 1% of the tweets, which means there are a lot of tweets that may not be collected around this topic. Second, the tweets collected are defined by hashtags that we curated, and we might have missed out some of them. The scoping by hashtag also can skew the emotions and context to fit the narrative by the hashtag and not the true feeling of discourse in general. Third, the emotional and sentiment tagging can still be inaccurate with respect of portraying the true emotion and sentiment of the tweet - as this is derived by an automated predictive approach with a ML library and not a human-tagged, gold-standard dataset. 

## Development Process
### Work Split
The work was split equally among the pair of team members. Adya did the data cleaning and overall design. Lynnette did the data collection and processing. Both contributed to the building of the interactive data science visualization. Exact word split and evolution can be observed in the commit history of our repository

### Time Spent
One week was spent collecting, processing and finalizing the dataset. Another week was spent wrangling with the Streamlit library.

### Aspects that took the most time
Two aspects took the most time: (a) data cleaning, in which we first did a manual inspection of the data, then performed exploratory data analysis to understand the distribution of the data and any duplicate and null values; (b) building the interaction in the visualization because we were not used to data visualization in Python.
