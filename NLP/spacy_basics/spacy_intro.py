# Tokenization and POS Tagging
'''spaCy’s tokenizer breaks text into words/punctuation; POS tagging labels them as nouns, verbs, etc.'''
import spacy 
nlp = spacy.load("en_core_web_sm")
doc = nlp("She eats apples.")
for token in doc:
    print(token.text , token.pos_)

# Named Entity Recognition (NER)
''' Identifies people, places, organizations, dates, etc.'''
doc = nlp("Apple was founded by Steve Jobs in California in 1976.")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Dependency Parsing
'''Analyzes sentence structure (who did what to whom).'''
for token in doc:
    print(token.text, "->", token.dep_, "->", token.head.text)

# Lemmatization (better than NLTK)
print([token.lemma_ for token in doc])

# ------ Task -------
'''Extract all person/entity names from "Elon Musk launched a rocket from Texas."'''
doc = nlp("Elon Musk launched a rocket from Texas.")
print([ent.text for ent in doc.ents if ent.label_ == "PERSON"])

# ------ Task - 2 --------
'''Given the text: <div>Learn AI with <b>PyTorch</b> @ 2023! Visit <a href="#">our site</a>.</div>

Remove all HTML tags.
Remove all non-alphanumeric characters (keep spaces).
Convert to lowercase.'''
import re 
from bs4 import BeautifulSoup

text = '<div>Learn AI with <b>PyTorch</b> @ 2023! Visit <a href="#">our site</a>.</div>'

# 1. Remove html tags
soup = BeautifulSoup(text,"html.parser")
text_no_html = soup.get_text()
print(f"Text without HTML: {text_no_html}")

# 2. Remove non-alphanumeric characters (keep spaces)
text_cleaned = re.sub(r'[^a-zA-Z0-9\s]','',text_no_html)
print(f"Text after special char removal:",{text_cleaned})

# 3. Convert to lowercase and clean extra spaces
final_text = re.sub(r'\s+',' ',text_cleaned).lower().strip()
print(f"Final Cleaned Text: '{final_text}")