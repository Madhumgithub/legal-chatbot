import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read legal text file
with open("legal_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split text into meaningful sections (paragraphs)
sections = text.split("\n\n")  # Assumes paragraphs are separated by double newline

# Remove empty sections and strip whitespace
sections = [section.strip() for section in sections if section.strip()]

# Generate embeddings for sections
embeddings = np.array([model.encode(section) for section in sections]).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance-based index
index.add(embeddings)

# Save the FAISS index
faiss.write_index(index, "legal_docs.index")

# Save processed legal sections for retrieval
with open("processed_legal_docs.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(sections))

print("Index built successfully!")
