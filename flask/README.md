## Flask Application for Sentiment Analysis

The Flask application in this project allows users to perform sentiment analysis on Reddit mental health posts.

**Link to Flask app: https://bit.ly/reddit-sentiment-analysis**

### Usage

#### Setting Up the Flask Application

1. Ensure you have Python installed on your system.
2. Install dependencies using `pip install -r flask/requirement.txt`.
3. Navigate to the `flask/flask_app` directory.
4. Create a virtual environment (optional but recommended):
```bash
   python -m venv venv
```
6. Activate the virtual environment:
```bash
   source venv/bin/activate
```
8. Install dependencies using `requirement.txt`:
```bash
pip install -r flask/requirement.txt
```

10. Run the Flask application using the following command:
```bash
   python app.py
```
12. Once the application is running, open a web browser and go to `http://localhost:2001/` to access the application.

#### Using the Application

- Enter a Reddit post related to mental health in the text area provided on the webpage.
- Click on the "Predict Sentiment" button to analyze the sentiment of the entered text.
- The sentiment (positive, negative, neutral) will be displayed along with relevant advice based on the sentiment category.

### Additional Notes

- The sentiment analysis model (`sentiment_model.joblib`) is used within the Flask application to classify the sentiment of input text.
- The `index.html` template and `style.css` file in the `templates` and `static` directories respectively provide the frontend interface for the Flask application.
- The `results_df.csv` file contains aggregated results from the analysis.
- This application aims to provide insights into sentiment trends in Reddit posts related to mental health.
