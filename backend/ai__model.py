import openai
import os
openai.api_key = os.getenv('OPENAI_API_KEY')
def generate_response(query):
    # Use OpenAI's GPT model to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )
    return response['choices'][0]['message']['content']
