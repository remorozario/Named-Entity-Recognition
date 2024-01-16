import spacy
import PyPDF2
import re

def extract_name(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)

    # Extract entities and filter for PERSON entities (names)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

    if names:
        return names[0]

    # If no PERSON entities are found, use a keyword-based approach
    keyword_patterns = [
        r'(?<=\b(?:Name|Full Name)\b\s*)[A-Z][a-z]+ [A-Z][a-z]+',
        # Add more patterns if needed
    ]

    for pattern in keyword_patterns:
        match = re.search(pattern, text)
        if match:
            return match.group()

    return None

# Rest of your existing code...
def pdf_to_text(pdf_file, text_file):
    try:
        # Open the PDF file
        with open(pdf_file, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Initialize an empty string to store the text
            text = ''
            
            # Iterate through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Extract text from the current page
                text += pdf_reader.pages[page_num].extract_text()
            
            # Extract the name from the text
            name = extract_name(text)

            with open(text_file, 'w', encoding='utf-8') as txt_file:
                # Write the name at the beginning of the file
                if name:
                    txt_file.write(name + '\n\n')
                # Write the rest of the text
                txt_file.write(text)
            
            print(f"Conversion successful! Text saved to '{text_file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    pdf_file = "C:/Users/HP/OneDrive/Desktop/cv's/Amal Full stack.pdf"
    text_file = "D:/NER/Named-Entity-Recognition/names.txt"

    # Extract text from PDF
    pdf_to_text(pdf_file, text_file)

    # Open the extracted text file and read its content
    with open(text_file, 'r', encoding='utf-8') as txt_file:
        resume_text = txt_file.read()

        # Extract the name using Spacy
        name = extract_name(resume_text)

        # Print the extracted name
        if name:
            print(f"Extracted Name: {name}")
        else:
            print("Name not found.")
