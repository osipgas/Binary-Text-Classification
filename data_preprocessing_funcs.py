import re
from scipy.sparse import hstack
from symbols_vectorizer import SymbolsVectorizer

# funcs for getting data

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

def remove_stopwords(mail):
    # initilizing stop words
    stop_words = set(stopwords.words('english'))
    # word tokenizing
    word_tokens = word_tokenize(mail)  
    # removing stop words
    filtered_sentence = [word for word in word_tokens if word not in stop_words]
    # concatinaing words back to string 
    return ' '.join(filtered_sentence)

def get_clean_mail(mail):
    # deleting everything except lower english letters and spaces
    mail = re.sub(r'[^a-z\s]', '', mail.lower())
    # deleting repetitive spaces
    mail = re.sub(r'\s+', ' ', mail)
    # removing stop words
    cleaned_text = remove_stopwords(mail.strip())
    return cleaned_text

def get_special_symbols(mail):
    # deleting everything except special symbols
    ssymbols = re.sub(r'[a-zA-Z0-9\s]', '', mail)
    return ssymbols

def vectorize_mail(text, special_symbols, text_vectorizer, special_symbols_vectorizer):
        # putting text in list if its not in the list to make function usable for a single text usage
        text = [text] if type(text) is not list else text
        special_symbols = [special_symbols] if type(special_symbols) is not list else special_symbols

        # vectorizing text
        text_vectorized = text_vectorizer.transform(text)
        # vectorizing special symbols
        special_symbols_vectorized = special_symbols_vectorizer.transform(special_symbols)
        # concatinaiting text_vectorized and special_symbols_vectorized to get x
        x = hstack([text_vectorized, special_symbols_vectorized])
        return x