from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_db, get_db
from ai__model import generate_response
from ml_model import predict_issue
from models import Ticket
import pandas as pd
import os 
app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv('OPENAI_API_KEY')
# Initialize cache
cache = {}


# @app.before_first_request
# def initialize():
init_db()


@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query')
    # Check if the response is cached
    if user_query in cache:
        return jsonify({'response': cache[user_query]})

    # Query the database for the response
    session = get_db()
    ticket = session.query(Ticket).filter_by(query=user_query).first()

    if ticket:
        response = ticket.response
    else:
        response = generate_response(user_query)  # Fallback to AI model
        # Optionally, save the new response to the database
        new_ticket = Ticket(query=user_query, response=response)
        session.add(new_ticket)
        session.commit()

    # Cache the response
    cache[user_query] = response
    return jsonify({'response': response})


@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    issue_data = data.get('issue_data')
    prediction = predict_issue(issue_data)
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True)
