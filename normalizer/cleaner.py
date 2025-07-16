import nltk
from nltk.corpus import stopwords

def to_lower(tokens: list) -> list:
    return [token.lower() for token in tokens]


try:
    stop_words = stopwords.words('russian')
except LookupError:
    nltk.download('stopwords')
    stop_words = stopwords.words('russian')

def remove_stopwords(tokens: list) -> list:
    return [token for token in tokens if token not in stop_words]