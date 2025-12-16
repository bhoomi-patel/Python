'''python -m pip install nltk
python -m nltk.downloader punkt stopwords wordnet omw-1.4 averaged_perceptron_tagger'''
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# 1. Tokenization
'''Splitting text into individual units—tokens—such as words or sentences.'''
import string
import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize
text = "NLTK makes NLP easy. Let's get started!"
word_tokens = word_tokenize(text)
sent_tokens = sent_tokenize(text)
print("Word Tokens:", word_tokens)
print("Sentence Tokens:", sent_tokens)

# 2. Stopwords Removal
'''Removing common words (like “the”, “is”, “and”) that carry less meaning.'''
from nltk.corpus import stopwords
nltk.download('stopwords')

text = "This is an example sentence."
stop_woords = set(stopwords.words('english'))
words = word_tokenize(text)
filtered = [w for w in words if w.lower() not in stop_woords]
print("Stopwords Removed:", filtered)

# 3. Stemming
'''Reducing words to their root form by chopping suffixes (e.g. running→run).'''
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print([stemmer.stem(w) for w in ['running','runs','easily','fairly']])

# 4. Lemmatization
'''Returns the actual dictionary base form of a word (run, not “runn”).'''
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
print([lemmatizer.lemmatize(w) for w in ['running','runs','easily','fairly']])

# 5. punctuation removal
words_no_punct = [word for word in words if word not in string.punctuation]
print(f"Tokens (no punctuation): {words_no_punct}")

# ------- Task -------
'''Spam Keyword Extractor
Read a sample SMS message.
Remove stopwords, apply stemming.
Output keywords for spam detection.'''
sms = "Congratulations! You've won a free iPhone. Click here now."
words = word_tokenize(sms)
filtered = [stemmer.stem(w) for w in words if w.lower() not in stop_woords and w.isalpha()]
print("Spam Keywords:",filtered)