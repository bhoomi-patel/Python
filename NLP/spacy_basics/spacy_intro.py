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