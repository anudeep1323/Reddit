# -*- coding: utf-8 -*-
"""Reddit sentiment analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ZElFNctsl8tKVaBI2xYY94Q0ZuAwlKW
"""

!pip install praw

!pip install transformers

import praw
from transformers import pipeline

reddit = praw.Reddit(client_id='i6PVGX6uZ1MfbUSJolrrbw',
                     client_secret='hz9Vut3NHyAx-kNOtODorlHklci5cw',
                     user_agent='aerogrampur')

subreddit_name = 'WorldNews'
subreddit = reddit.subreddit(subreddit_name)

top_posts = list(subreddit.top(limit=10000))  # Retrieve the top 10 posts

for post in top_posts:
    print(post.title)

from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Load the sentiment analysis model and tokenizer
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a sentiment analysis pipeline with the specified model
sentiment_analysis = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Now you can use the sentiment analysis pipeline as before




sentiment_analysis = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
for post in top_posts:
    title = post.title
    sentiment_result = sentiment_analysis(title)

    sentiment_label = sentiment_result[0]['label']
    if sentiment_label == 'POSITIVE':
        positive_count += 1
    elif sentiment_label == 'NEGATIVE':
        negative_count += 1
    else:
        neutral_count += 1

    print(f"Title: {title}")
    print(f"Sentiment: {sentiment_label} with confidence {sentiment_result[0]['score']}")
    print("-" * 50)

print(f"Number of posts: {len(list(top_posts))}")
positive_count = 0
negative_count = 0
neutral_count = 0

# Apply sentiment analysis to each post's title
for post in top_posts:
    title = post.title
    sentiment_result = sentiment_analysis(title)

    # Determine the sentiment label and update counts
    sentiment_label = sentiment_result[0]['label']
    if sentiment_label == 'POSITIVE':
        positive_count += 1
    elif sentiment_label == 'NEGATIVE':
        negative_count += 1
    else:
        neutral_count += 1

    print(f"Title: {title}")
    print(f"Sentiment: {sentiment_label} with confidence {sentiment_result[0]['score']}")
    print("-" * 50)

# Calculate percentages only if there are posts
if total_posts > 0:
    positive_percentage = (positive_count / total_posts) * 100
    negative_percentage = (negative_count / total_posts) * 100
    neutral_percentage = (neutral_count / total_posts) * 100

    # Print the results
    print("\nSentiment Analysis Results:")
    print(f"Positive: {positive_percentage:.2f}%")
    print(f"Negative: {negative_percentage:.2f}%")
    print(f"Neutral: {neutral_percentage:.2f}%")
else:
    print("\nNo posts to analyze.")