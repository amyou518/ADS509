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
- `descriptive_statistics.ipynb`: Jupyter Notebook containing the analysis of descriptive statistics for both subreddits.

### Prerequisites
To run the analysis, make sure you have the following installed:
- Python 3.x
- `praw` library
- `pandas` library
- `nltk` library (with WordNet, punkt, stopwords datasets downloaded)
