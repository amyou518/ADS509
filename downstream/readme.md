
## Sentiment Analysis and Word Cloud Generation

This repository contains code for performing sentiment analysis on text data and generating word clouds for different sentiment labels. The goal is to visualize the most frequent words in positive, negative, and neutral sentiment texts.

## Table of Contents
- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Sentiment Analysis](#sentiment-analysis)
- [Word Cloud Generation](#word-cloud-generation)
- [Results](#results)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Data Preparation

Ensure your data is in a CSV file with at least the following columns:
- `sentiment`: The sentiment label (e.g., positive, negative, neutral).
- `selftext`: The raw text data.

If your text data is not preprocessed, the code will preprocess it to create a `processed_text` column.

## Sentiment Analysis

The sentiment analysis is performed using pre-trained models to classify text data into positive, negative, and neutral categories. The classification results are stored in the DataFrame for further analysis.

## Word Cloud Generation

We generate word clouds for each sentiment label to visualize the most frequent words in each category. This helps in understanding the common themes and keywords associated with each sentiment.

## Results

We have used different models like  Logistic Regression  Support Vector Machine, Random Forest, XGBoost, K-Nearest Neighbors. But among them random forest shows the better result. 
