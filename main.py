from normalizer.tokenizer import tokenize
from normalizer.cleaner import to_lower, remove_stopwords
from normalizer.spellchecker import correct_spelling
from normalizer.lemmatizer import lemmatize

text = "текста люблю я ловил"

tokens = tokenize(text)
tokens = to_lower(tokens)
tokens = remove_stopwords(tokens)
tokens = correct_spelling(tokens)
tokens = lemmatize(tokens)

print("Результат:", tokens)
