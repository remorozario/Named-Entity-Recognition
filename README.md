## Automated Resume Parsing

An automated resume parsing tool that streamlines the recruitment process by extracting key information from candidate resumes. This tool uses advanced Natural Language Processing (NLP) and machine learning techniques to extract details like contact information, work experience, education, skills, and certifications, reducing manual processing time by over 50%.

## Table of Contents
- Technologies Used
- Features
- Installation
- Usage
- Project Structure
- Contributing
- License

## Technologies Used
- **Python**: Core programming language for building the tool.
- **Natural Language Toolkit (NLTK)**: Used for NLP preprocessing tasks.
- **spaCy**: Used for entity recognition and NLP processing.
- **scikit-learn**: Implemented machine learning algorithms to improve extraction accuracy.
- **Flask**: Web framework for developing the user interface.
- **Pandas**: Data manipulation and analysis.
- **Git**: Version control.

## Features
- **Automated Parsing**: Extracts key information like contact details, work experience, education, skills, and certifications from resumes.
- **Enhanced NLP Techniques**: Uses NLP to improve the accuracy of information extraction.
- **User-Friendly Interface**: A simple and intuitive interface that allows recruiters to upload resumes in PDF format and view parsed data in an organized manner.
- **Rigorous Testing and Validation**: Tested against diverse resume datasets to ensure high accuracy and reduce false positives.
- **Improved Accuracy with Machine Learning**: Achieved a 60% accuracy improvement in information extraction using machine learning algorithms.

## Installation
1. Clone the repository:
     ```bash
   git clone https://github.com/yourusername/automated-resume-parsing.git
   cd automated-resume-parsing

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Set up the Flask application:
    ```bash
    export FLASK_APP=app.py

## Usage
1. Start the Flask server:
    ```bash
    flask run
2. Access the tool at http://127.0.0.1:5000.
3. Upload a resume in PDF format and view the parsed data.

## Project Structure
```
├── app.py             # Flask application entry point
├── parser.py          # Resume parsing logic
├── templates/         # HTML templates for the web interface
├── static/            # Static files (CSS, JS)
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation
```
## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

This `README.md` includes sections on features, installation, usage, project structure, and contribution guidelines. Update the GitHub link under "Installation" to your repository's actual URL.