from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import re

app = Flask(__name__)

# Configure Google Generative AI with your API key
genai.configure(api_key="API Key")

# Configure the generative model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # Adjust safety settings if needed
)

def format_response(text):
    # Replace asterisks with HTML bold tags
    text = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', text)
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]

    # Format user input to interpret asterisks for bold text
    user_input_formatted = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', user_input)

    chat_session = model.start_chat(
        history=[
            {"role": "user", "parts": [user_input_formatted]},
        ]
    )

    response = chat_session.send_message(user_input_formatted)
    formatted_response = format_response(response.text)

    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    app.run(debug=True)
