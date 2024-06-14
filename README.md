# Exploring Mental Health Discourse on Reddit

This repository contains code and data for analyzing posts from two Reddit communities: `r/MentalHealth` and `r/MentalHealthSupport`. The data was retrieved using the Reddit API via the `praw` library. The dataset is aimed at understanding discussions around mental health on these platforms.

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

- `reddit_posts.csv`: The combined dataset of posts from `r/MentalHealth` and `r/MentalHealthSupport`.

### Prerequisites
- Python 3.x
- `praw` library
- `pandas` library



