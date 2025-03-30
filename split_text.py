import os

def split_text_into_chunks(text, chunk_size=500):
    """Splits text into chunks of a given size."""
    words = text.split()
    chunks = [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Step 1: Load the merged legal text
with open("legal_text.txt", "r", encoding="utf-8") as f:
    legal_text = f.read()

# Step 2: Split text into chunks
text_chunks = split_text_into_chunks(legal_text)

# Step 3: Save chunks into a new folder
output_dir = "processed_data"  # Folder to store chunks
os.makedirs(output_dir, exist_ok=True)  # Create folder if not exists

for i, chunk in enumerate(text_chunks):
    with open(f"{output_dir}/chunk_{i}.txt", "w", encoding="utf-8") as f:
        f.write(chunk)

print(f"✅ Text split into {len(text_chunks)} chunks and saved in '{output_dir}' folder.")
