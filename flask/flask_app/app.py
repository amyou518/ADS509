from flask import Flask, render_template, request, jsonify
import joblib
import os

model_filename = 'sentiment_model.joblib'
model_path = os.path.join(os.path.dirname(__file__), model_filename)

app = Flask(__name__)

# Load the sentiment analysis model
try:
    sentiment_pipeline = joblib.load(model_path)
except FileNotFoundError as e:
    print(f"Model file '{model_path}' not found. Error: {e}")
    sentiment_pipeline = None
except Exception as e:
    print(f"Error loading model from '{model_path}': {e}")
    sentiment_pipeline = None

# Function to classify sentiment and generate advice
def classify_sentiment(text):
    try:
        sentiment_result = sentiment_pipeline.predict([text])[0]
        
        # Example: Extracting sentiment information
        sentiment = sentiment_result.get('sentiment', 'neutral')
        sentiment_category = sentiment_result.get('sentiment_category', 'unknown')
        sentiment_score = sentiment_result.get('sentiment_score', 0.0)
        
        # Generate advice based on sentiment
        advice = ''
        if sentiment == 'negative':
            advice = 'Consider seeking help or support from mental health professionals or advocates. Here are some resources:'
            advice += '<br><a class="link" href="https://www.samhsa.gov/find-help/national-helpline">SAMHSA National Helpline</a>'
            advice += '<br><a class="link" href="https://www.teleclearrecoverycenter.com/lp/mentalhealthtreatment/?campaignid=14464604393&adgroupid=125388300166&creative=629210324347&matchtype=e&network=g&device=c&keyword=mental%20health%20professionals%20near%20me&gad_source=1&gclid=EAIaIQobChMIovL2jMvthgMV8GlHAR1MOw5eEAAYASAAEgIGK_D_BwE">Teleclear Recovery Center</a>'
            advice += '<br><a class="link" href="https://findtreatment.gov">FindTreatment.gov</a>'
        
        return {
            'sentiment': sentiment,
            'sentiment_category': sentiment_category,
            'sentiment_score': sentiment_score,
            'advice': advice
        }
    
    except Exception as e:
        print(f"Error classifying sentiment: {e}")
        return {
            'sentiment': 'neutral',
            'sentiment_category': 'unknown',
            'sentiment_score': 0.0,
            'advice': ''
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': 'MissingInputError', 'message': 'Missing text input'}), 400
        
        text = data['text']
        
        # Perform sentiment analysis and get advice
        sentiment_result = classify_sentiment(text)
        
        # Prepare response JSON
        response = {
            'sentiment': sentiment_result['sentiment'],
            'sentiment_category': sentiment_result['sentiment_category'],
            'sentiment_score': sentiment_result['sentiment_score'],
            'advice': sentiment_result['advice']
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': 'UnexpectedError', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
