from flask import Flask, request, jsonify
import traceback
from utils.executor import handle_question
import os

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def analyze():
    try:
        question_file = request.files.get('questions.txt')
        if not question_file:
            return jsonify({"error": "Missing questions.txt"}), 400

        questions = question_file.read().decode('utf-8')
        files = {f.filename: f for f in request.files.values() if f.filename != 'questions.txt'}

        result = handle_question(questions, files)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    app.run(debug=True)
