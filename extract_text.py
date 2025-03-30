import fitz  # PyMuPDF

# File Paths (Use Double Backslashes or Raw Strings)
ipc_path = r"C:\Users\MSP\legal-chatbot\legal_documents\Indian_Penal_Code.pdf"
constitution_path = r"C:\Users\MSP\legal-chatbot\legal_documents\Constitution_of_India.pdf"
case_law_path = r"C:\Users\MSP\legal-chatbot\legal_documents\Supreme_Court_Case_Laws.pdf"

# Function to Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

# Extract text from each legal document
ipc_text = extract_text_from_pdf(ipc_path)
constitution_text = extract_text_from_pdf(constitution_path)
case_law_text = extract_text_from_pdf(case_law_path)

# Save extracted text to .txt files
with open("ipc.txt", "w", encoding="utf-8") as f:
    f.write(ipc_text)

with open("constitution.txt", "w", encoding="utf-8") as f:
    f.write(constitution_text)

with open("case_law.txt", "w", encoding="utf-8") as f:
    f.write(case_law_text)

print("Text extraction complete. Files saved as ipc.txt, constitution.txt, and case_law.txt")
