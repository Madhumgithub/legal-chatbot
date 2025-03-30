import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Step 1: Load Sentence Transformer Model
print("📌 Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Step 2: Load text chunks
output_dir = "processed_data"

# Only include valid chunk files (ignoring other files)
chunk_files = [
    f for f in os.listdir(output_dir) if f.startswith("chunk_") and f.endswith(".txt")
]

# Sort numerically
chunk_files = sorted(chunk_files, key=lambda x: int(x.split("_")[1].split(".")[0]))

text_chunks = [open(f"{output_dir}/{file}", "r", encoding="utf-8").read() for file in chunk_files]

print(f"📌 Loaded {len(text_chunks)} text chunks.")

# Step 3: Convert text chunks into embeddings
print("📌 Generating embeddings for text chunks...")
chunk_vectors = model.encode(text_chunks)

# Step 4: Create FAISS index
d = chunk_vectors.shape[1]  # Dimension of embeddings
index = faiss.IndexFlatL2(d)  # L2 distance-based index
index.add(np.array(chunk_vectors))  # Add embeddings to index

# Step 5: Save FAISS index
faiss.write_index(index, "legal_chunks_index.faiss")

# Step 6: Save text chunk mapping
with open("legal_chunks_map.pkl", "wb") as f:
    pickle.dump({i: text for i, text in enumerate(text_chunks)}, f)

print("✅ FAISS index created and saved successfully.")
