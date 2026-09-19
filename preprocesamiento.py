import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download("stopwords", quiet=True)
stopwords_es = set(stopwords.words("spanish")) 

def text_preprocess(text):
    tokenizer = RegexpTokenizer(r'[a-zA-ZáéíóúñÁÉÍÓÚÑüÜ]+')
    stemmer = SnowballStemmer('spanish')
    tokens = tokenizer.tokenize(text.lower())
    tokens = [t for t in tokens if t not in stopwords_es]
    tokens = [stemmer.stem(t) for t in tokens]
    return ' '.join(tokens)