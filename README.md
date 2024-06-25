# Exploring Mental Health Discourse on Reddit

## Contributors 
Amy Ou, S M Sultan Mahmud Rahat, and Samantha Rivas 

1. [Analysis Goals](#analysis-goals)
2. [Methodology](#methodology)
3. [Dataset Description](#dataset-description)
   - [Data Source](#data-source)
   - [Number of Variables](#number-of-variables)
   - [Dataset Size](#dataset-size)
4. [Repository Contents](#repository-contents)
   - [data/](#data)
   - [downstream/](#downstream)
   - [flask/](#flask)
   - [Jupyter Notebooks](#jupyter-notebooks)
5. [Prerequisites](#prerequisites)
6. [Usage](#usage)
7. [License](#license)

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
- **data/**: Directory containing datasets used for analysis:
  - `mental_health_posts.csv`: Data from `r/MentalHealth`.
  - `mental_health_support_posts.csv`: Data from `r/MentalHealthSupport`.
  - `reddit_posts.csv`: Combined dataset from both subreddits.
  - `mental_health_posts_cleaned.csv`: Cleaned data for `r/MentalHealth`.
  - `mental_health_support_posts_cleaned.csv`: Cleaned data for `r/MentalHealthSupport`.
  - `reddit_posts.csv_cleaned`: Cleaned combined dataset.

- **downstream/**: Directory containing downstream data analysis:
  - `readme.md`: Detailed description of downstream analysis.
  - `requirement.txt`: Dependency list for downstream analysis.
  - `results_df.csv`: Aggregated results from analysis.
  - `sentiment_analysis.csv`: Additional sentiment-related analysis results.
  - `lda_visualization.html`: HTML file containing interactive visualizations and insights generated from topic modeling using Latent Dirichlet Allocation (LDA). This file visually represents the identified topics within the subreddit data, providing a deeper understanding of the thematic structure and discussions.

- **flask/**: Directory with Flask application for sentiment analysis:
  - `requirement.txt`: Dependencies for Flask application.
  - `readme.md`: Description of the Flask application.
  - **flask_app/**: Files for Flask application:
    - `app.py`: Main script for Flask application.
    - `sentiment_model.joblib`: Model file for sentiment analysis.
    - **templates/**: HTML templates for Flask app.
    - **static/**: Static assets (e.g., CSS files).

- **Jupyter Notebooks**: Notebooks focusing on different aspects of the analysis:
  - `reddit_mental_health_posts_extraction.ipynb`: Data extraction from Reddit related to mental health.
  - `reddit_mental_health_posts_analysis.ipynb`: Tokenization, normalization, and descriptive statistics of Reddit posts.
  - `reddit_mental_health_posts_downstream.ipynb`: Advanced text analysis and machine learning techniques for sentiment analysis and topic modeling in `r/MentalHealth` and `r/MentalHealthSupport` communities.


### Prerequisites
To run the analysis, make sure you have the following installed:
- Python 3.x
- `praw` library
- `pandas` library
- `nltk` library (with WordNet, punkt, stopwords datasets downloaded)

## Usage

To replicate this analysis on your local machine, follow these steps:

1. Clone this repository to your local environment.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
4. Navigate to each directory (e.g., `flask/flask_app`, `downstream`) and follow the setup instructions provided in their respective `README.md` files.
5. Open and run the Jupyter notebooks in the `reddit_mental_health_posts_analysis.ipynb` and `reddit_mental_health_posts_downstream.ipynb` to explore the data and perform detailed analysis.
6. Start the Flask application as described in `flask/README.md` to interactively analyze sentiment of Reddit posts in real-time.

## License

This project is licensed under the [MIT License](LICENSE).
