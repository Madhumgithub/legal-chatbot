import pandas as pd
from chatbot import chatbot_response  # Ensure chatbot.py exists

# Load test data
df = pd.read_csv("test_questions.csv")

# Evaluate chatbot responses
def evaluate():
    correct = 0
    total = len(df)

    for index, row in df.iterrows():
        question = row["question"]
        expected_answer = row["expected_answer"]
        bot_answer = chatbot_response(question)  # Get response from chatbot
        
        print(f"Q: {question}")
        print(f"Bot: {bot_answer}")
        print(f"Expected: {expected_answer}\n")

        if expected_answer.lower() in bot_answer.lower():
            correct += 1

    accuracy = (correct / total) * 100
    print(f"Chatbot Accuracy: {accuracy:.2f}%")

# Run evaluation
if __name__ == "__main__":
    evaluate()
