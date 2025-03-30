import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load pre-trained model for text embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def convert_text_to_vector(text):
    return model.encode(text)

# Load FAISS index (Make sure 'legal_index.faiss' exists)
index = faiss.read_index("legal_index.faiss")

def get_text_from_index(index_id):
    # Retrieve text from database or dictionary
    legal_docs = {
        0: "A landlord must provide notice before eviction.",
        1: "A tenant has the right to dispute an eviction notice in court.",
        # Add more legal documents here...
    }
    return legal_docs.get(index_id, "No relevant information found.")

def search_legal_docs(query):
    query_vector = np.array([convert_text_to_vector(query)]).astype("float32")

    # Search FAISS index for relevant laws
    D, I = index.search(query_vector, k=5)  # Top 5 results

    results = [get_text_from_index(i) for i in I[0] if i >= 0]
    return results if results else ["No relevant legal information found."]
