import nltk
from nltk.tokenize import word_tokenize

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


def tokenize(text: str) -> list:

    if not isinstance(text, str):
        text = str(text)
    # Используем word_tokenize для разбивки
    tokens = word_tokenize(text)
    return tokens
