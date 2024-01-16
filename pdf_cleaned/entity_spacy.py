import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Your text
text = """
"""

# Process the text with spaCy
doc = nlp(text)

# Extract named entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Print identified entities
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
