import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def clean_resume_text(resume_text):
    # Lowercasing
    resume_text = resume_text.lower()
    
    # Tokenization
    words = word_tokenize(resume_text)
    
    # Removing punctuation
    words = [word for word in words if word not in string.punctuation]
    
    # Reconstruct the text
    resume_text = ' '.join(words)
    
    # Handling whitespace and line breaks
    resume_text = re.sub(r'\s+', ' ', resume_text)
    
    # Stop word removal
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(resume_text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Reconstruct the text
    resume_text = ' '.join(filtered_words)
    
    # Lemmatization (using WordNet lemmatizer)
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(resume_text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    
    # Reconstruct the text
    resume_text = ' '.join(lemmatized_words)
    
    # Handling leading/trailing whitespaces
    resume_text = resume_text.strip()
    
    return resume_text

# Specify the path to your resume text file
resume_file_path = "D:/NER/Named-Entity-Recognition/pdf.txt" # Replace with the actual file path

# Read the resume text from the file
with open(resume_file_path, 'r', encoding='utf-8') as file:
    resume_text = file.read()

# Clean the resume text
cleaned_resume_text = clean_resume_text(resume_text)

# Print the cleaned resume text
print(cleaned_resume_text)

# Specify the path to the output text file where you want to save the cleaned text
output_file_path = "cleaned_resume_text.txt"

# Write the cleaned text to the output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_resume_text)

print(f"Cleaned text saved to {output_file_path}")