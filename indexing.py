import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load extracted legal text
with open("legal_text.txt", "r", encoding="utf-8") as f:
    sentences = f.readlines()

# Encode sentences into vectors
sentence_vectors = model.encode(sentences)

# Create FAISS index
index = faiss.IndexFlatL2(sentence_vectors.shape[1])
index.add(np.array(sentence_vectors))

# Save FAISS index
faiss.write_index(index, "legal_index.faiss")

# Save sentence mapping
with open("sentence_map.pkl", "wb") as f:
    pickle.dump(sentences, f)

print("FAISS index created and saved as legal_index.faiss")
