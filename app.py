from flask import Flask, request, jsonify
from flask_cors import CORS
from search_faiss import search_legal_docs

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if "question" not in data:
        return jsonify({"error": "Missing 'question' field"}), 400

    response = search_legal_docs(data["question"])
    return jsonify({"answer": "\n\n".join(response)})  # Clean output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
