import PyPDF2

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
            
            # Write the extracted text to the text file
            with open(text_file, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            
            print(f"Conversion successful! Text saved to '{text_file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    pdf_file = "C:/Users/HP/OneDrive/Desktop/Remo_Rozario_ML_Resume.pdf"  # Replace with the path to your PDF file
    text_file = "D:/NER/Named-Entity-Recognition/pdf.txt"  # Replace with the desired output text file
    
    pdf_to_text(pdf_file, text_file)