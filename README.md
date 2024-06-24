# Exploring Mental Health Discourse on Reddit

## Analysis Goals

This project aims to analyze and understand the discourse surrounding mental health topics on Reddit, specifically focusing on the communities of `r/MentalHealth` and `r/MentalHealthSupport`. The analysis will explore patterns in posts, sentiment expressed, and common topics discussed within these communities.

## Methodology

The data was collected using the Reddit API through the `praw` library in Python. Each subreddit's posts were retrieved, cleaned, and processed using `pandas` and `nltk` for natural language processing tasks such as tokenization and sentiment analysis. Descriptive statistics were calculated to provide insights into post characteristics and community engagement.

## Dataset Description

### Data Source
The data was collected from Reddit communities:
- **r/MentalHealth**: A community focused on general mental health topics.
- **r/MentalHealthSupport**: A support-oriented community for individuals seeking help and advice related to mental health issues.

### Number of Variables
The dataset contains 13 variables:
1. `title`: Title of the Reddit post.
2. `score`: The score of the post.
3. `upvote_ratio`: The upvote ratio of the post.
4. `created_utc`: The creation time of the post in UTC.
5. `selftext`: The text content of the post.
6. `subreddit`: The subreddit from which the post was retrieved.
7. `author`: The author of the post.
8. `media_only`: A boolean indicating if the post contains only media.
9. `permalink`: The permalink to the post.
10. `num_comments`: The number of comments on the post.
11. `upvotes`: The number of upvotes the post received.
12. `downvotes`: The number of downvotes the post received.
13. `upvotes/subscribers`: The ratio of upvotes to the number of subscribers in the subreddit.

### Dataset Size
The combined dataset contains 3,977 entries.

## Repository Contents
- `data/`: Folder containing the following datasets used for analysis:
  - `mental_health_posts.csv`: Dataset from `r/MentalHealth`.
  - `mental_health_support_posts.csv`: Dataset from `r/MentalHealthSupport`.
  - `reddit_posts.csv`: The combined dataset of posts from both subreddits.
  - `mental_health_posts_cleaned.csv`: Cleaned dataset after normalization and tokenization for `r/MentalHealth`.
  - `mental_health_support_posts_cleaned.csv`: Cleaned dataset after normalization and tokenization for `r/MentalHealthSupport`.
  - `reddit_posts.csv_cleaned`: Cleaned dataset after normalization and tokenization for the combined dataset.

- `downstream/`: Directory containing downstream data results:
  - `readme.md`: Detailed description of the downstream analysis.
  - `requirement.txt`: File listing dependencies for downstream analysis.
  - `results_df.csv`: Aggregated results from the analysis.
  - `sentiment_analysis.csv`: Additional analysis results related to sentiment.
    
- `flask/`: Directory containing Flask application for sentiment analysis:
  - `requirement.txt`: File listing dependencies for the Flask application.
  - `readme.md`: Detailed description of the Flask application.
  - `flask_app/`: Directory containing Flask application files:
    - `app.py`: Main Flask application script.
    - `sentiment_model.joblib`: Sentiment analysis model file.
    - `templates/`: Directory containing HTML templates for the Flask app.
    - `static/`: Directory containing static assets (e.g., CSS stylesheets).
      
- `reddit_mental_health_posts_extraction.ipynb`: Focuses on data retrieval and extraction of Reddit posts related to mental health.
- `reddit_mental_health_posts_analysis.ipynb`: Focuses on tokenization, normalization, and descriptive statistics analysis of Reddit posts related to mental health.
- `reddit_mental_health_posts_modeling.ipynb`: Focuses on advanced text analysis and machine learning techniques to explore sentiment patterns and topic modeling within `r/MentalHealth` and `r/MentalHealthSupport` Reddit communities.

### Prerequisites
To run the analysis, make sure you have the following installed:
- Python 3.x
- `praw` library
- `pandas` library
- `nltk` library (with WordNet, punkt, stopwords datasets downloaded)
