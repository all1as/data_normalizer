import inspect
from collections import namedtuple

ArgSpec = namedtuple('ArgSpec', ['args', 'varargs', 'keywords', 'defaults'])
def _getargspec(func):
    full = inspect.getfullargspec(func)
    return ArgSpec(args=full.args, varargs=full.varargs, keywords=full.varkw, defaults=full.defaults)
inspect.getargspec = _getargspec

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def lemmatize(tokens: list) -> list:
    lemmatized = []
    for token in tokens:
        if token.isalpha():
            parsed = morph.parse(token)
            lemma = parsed[0].normal_form if parsed else token
            lemmatized.append(lemma)
        else:
            lemmatized.append(token)
    return lemmatized