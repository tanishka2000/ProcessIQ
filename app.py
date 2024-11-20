import base64
import io

from flask import Flask, render_template, request, jsonify
from utills.constants import PNID_PROMPT
from utills.genai import genai_response
from utills.pnid import generate_pid

# Initialize Flask app
app = Flask(__name__)

# Initialize chat history
chat_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo')
def demo():
    """Render the chat UI."""
    return render_template('demo.html', chat_history=chat_history)

@app.route('/ask', methods=['POST'])
def ask():
    """Handle user questions and return chatbot responses."""
    data = request.json
    user_request = data.get("question", "") + PNID_PROMPT
    if not user_request:
        return jsonify({"error": "No question provided"}), 400

    # Generate response using the Gemini model
    bot_response = genai_response(user_request, chat_history)

    if not bot_response:
        return jsonify({"error": "Failed to get bot response"}), 500

    # Generate the P&ID diagram
    fig = generate_pid(bot_response)

    # Convert the figure to a base64 string
    img_io = io.BytesIO()
    if fig:
        fig.savefig(img_io, format='png')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('ascii')
        img_url = f"data:image/png;base64,{img_base64}"
    else:
        img_url = None

    return jsonify({
        "genai_response": bot_response,
        "p_id_data": img_url
    })

if __name__ == '__main__':
    app.run(debug=True)
