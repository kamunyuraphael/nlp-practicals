import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

text = 'Natural Language Processing is fascinating'
tokens = word_tokenize(text)
print(tokens)
