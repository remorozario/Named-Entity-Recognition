import re
import PyPDF2

def extract_name(text):
    # Use regular expression to find a pattern that looks like a name
    name_pattern = re.compile(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b')
    matches = name_pattern.findall(text)
    if matches:
        return matches[0]
    else:
        return None

# def extract_name(text):
#     # Search for the name "REMO ROZARIO" in the text
#     name_pattern = re.compile(r'REMO ROZARIO', re.IGNORECASE)
#     match = name_pattern.search(text)
#     if match:
#         return match.group()
#     else:
#         return None



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

            # Write the extracted text to the text file
            with open(text_file, 'w', encoding='utf-8') as txt_file:
                # Write the name at the beginning of the file
                if name:
                    txt_file.write(name + '\n\n')
                # Write the rest of the text
                txt_file.write(text)
            
            print(f"Conversion successful! Text saved to '{text_file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# # Add this line before writing to the text file
# print(f"Extracted Text: {text_file}")

if __name__ == "__main__":
    pdf_file = "C:/Users/HP/OneDrive/Desktop/Remo_Rozario_ML_Resume.pdf"  # Replace with the path to your PDF file
    text_file = "D:/NER/Named-Entity-Recognition/name.txt"  # Replace with the desired output text file
    
    pdf_to_text(pdf_file, text_file)
