import os

# Define the file paths
input_files = ["ipc.txt", "constitution.txt", "case_law.txt"]
output_file = "legal_text.txt"

# Merge all files into one
with open(output_file, "w", encoding="utf-8") as outfile:
    for file in input_files:
        with open(file, "r", encoding="utf-8") as infile:
            outfile.write(infile.read() + "\n\n")

print(f"✅ Merged {len(input_files)} files into '{output_file}'")
