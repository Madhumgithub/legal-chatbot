Legal Chatbot
=============

A legal chatbot powered by Python, Flask, and LangChain to provide legal assistance by answering user queries.

------------------------------------------------------

🚀 Features:
-------------
- Provides legal information
- Uses NLP and LangChain for responses
- Accepts user queries via API
- Utilizes FAISS for efficient retrieval
- Flask backend for easy deployment

------------------------------------------------------

🛠️ Tech Stack:
---------------
- Python
- Flask
- LangChain
- FAISS
- OpenAI API (if applicable)

------------------------------------------------------

📂 Project Structure:
----------------------
legal-chatbot/
│── env/                 - Virtual environment (excluded from Git)
│── data/                - Legal documents dataset
│── models/              - AI models (if applicable)
│── legal_index.faiss    - FAISS index file
│── app.py               - Main Flask app
│── chatbot.py           - Chatbot logic using LangChain
│── requirements.txt     - Dependencies
│── README.txt           - Project documentation
│── .gitignore           - Git ignore file

------------------------------------------------------

💻 Setup & Installation:
------------------------

1️⃣ Clone the Repository:
------------------------
git clone https://github.com/your-username/legal-chatbot.git
cd legal-chatbot

2️⃣ Create & Activate Virtual Environment:
------------------------------------------
For Windows:
python -m venv env
env\Scripts\activate

For macOS/Linux:
python3 -m venv env
source env/bin/activate

3️⃣ Install Dependencies:
-------------------------
pip install -r requirements.txt

4️⃣ Run the Chatbot:
-------------------
python app.py

The API will be available at:
http://127.0.0.1:5000/chat

------------------------------------------------------

🛠️ API Usage:
--------------

POST /chat:
-----------
Send a JSON request with a legal question:

{
  "question": "How can I evict a tenant legally?"
}

Example cURL Command:
----------------------
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{\"question\": \"How can I evict a tenant legally?\"}"

Response Example:
-----------------
{
  "answer": "You must provide a written notice according to state laws..."
}

------------------------------------------------------

📜 License:
-----------
This project is licensed under the MIT License.

------------------------------------------------------

📬 Contact & Contributions:
---------------------------
Contributions are welcome! Fork, modify, and submit a PR.
Contact: mp9075@srmist.edu.in
