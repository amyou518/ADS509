from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Define the path to the model in the same directory
model_path = os.path.join(os.path.dirname(__file__), 'sentiment_model.joblib')

# Load the model
sentiment_model = joblib.load(model_path)

# Function to classify sentiment as negative, positive, or neutral
def classify_sentiment(text):
    try:
        sentiment = sentiment_model.predict([text])[0]
        if sentiment == 'negative':
            advice = 'Consider seeking help or support from mental health professionals or advocates. Here are some resources:'
            advice += '<br><a class="link" href="https://www.samhsa.gov/find-help/national-helpline">SAMHSA National Helpline</a>'
            advice += '<br><a class="link" href="https://www.teleclearrecoverycenter.com/lp/mentalhealthtreatment/?campaignid=14464604393&adgroupid=125388300166&creative=629210324347&matchtype=e&network=g&device=c&keyword=mental%20health%20professionals%20near%20me&gad_source=1&gclid=EAIaIQobChMIovL2jMvthgMV8GlHAR1MOw5eEAAYASAAEgIGK_D_BwE">Teleclear Recovery Center</a>'
            advice += '<br><a class="link" href="https://findtreatment.gov">FindTreatment.gov</a>'
            return 'negative', advice
        elif sentiment == 'positive':
            return 'positive', ''
        else:
            return 'neutral', ''
    except Exception as e:
        print(f"Error classifying sentiment: {e}")
        return 'neutral', ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if text:
        sentiment, advice = classify_sentiment(text)
        return jsonify({'sentiment': sentiment, 'advice': advice})
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
