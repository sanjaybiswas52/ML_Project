from docx import Document
import os

def extract_text_from_docx(file_path, output_path):
    """
    Extracts text from a .docx file and saves it to a .txt file.
    
    :param file_path: Path to the .docx file.
    :param output_path: Path to save the extracted .txt file.
    """
    doc = Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the extracted text
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Text extracted and saved to {output_path}")


# Extract and save text
#extract_text_from_docx('/Users/sanjaybiswas/Downloads/ATS-G-1807-AJAY RAJ WAZIR-A.docx', '/Users/sanjaybiswas/Downloads/ATS-G-1807.text')
