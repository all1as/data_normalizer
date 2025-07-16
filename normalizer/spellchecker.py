from pyaspeller import YandexSpeller
from nltk.tokenize import word_tokenize

speller = YandexSpeller(lang='ru')

def correct_spelling(tokens: list) -> list:
    text = ' '.join(tokens)
    corrected_text = speller.spelled(text)
    return word_tokenize(corrected_text) if isinstance(corrected_text, str) else tokens
