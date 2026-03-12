import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import SnowballStemmer

# Stopwords en inglés, pero conservando negaciones importantes
stop_words = set(ENGLISH_STOP_WORDS)
palabras_negativas = {"no", "nor", "not", "didn", "didn't", "wasn", "wasn't"}
stop_words = stop_words - palabras_negativas

stemmer = SnowballStemmer("english")

def limpiar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^\w\s]", "", texto)
    tokens = texto.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)