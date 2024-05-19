from data_preprocessing_funcs import get_clean_mail, get_special_symbols, vectorize_mail

# The spam filter

class SpamFilter:
    def __init__(self, model, text_vectorizer, special_symbols_vectorizer):
        self.model = model
        self.text_vectorizer = text_vectorizer
        self.special_symbols_vectorizer = special_symbols_vectorizer
    
    def check(self, mail):
        # getting clean text and special symbols
        text = get_clean_mail(mail)
        special_symbols = get_special_symbols(mail)
        # vectorizing and concatinaiting text and special_symbols with vectorize_mail function
        x = vectorize_mail(text, special_symbols, self.text_vectorizer, self.special_symbols_vectorizer)
        # making prediction
        prediction = self.model.predict(x)[0]
        return "Spam" if prediction == 1 else "Ham"
    
    def check_multiply(self, mails):
        # getting clean text and special symbols lists
        text_list = [get_clean_mail(mail) for mail in mails]
        special_symbols_list = [get_special_symbols(mail) for mail in mails]
        # vectorizing and concatinaiting text and special_symbols with vectorize_mail function
        x = vectorize_mail(text_list, special_symbols_list, self.text_vectorizer, self.special_symbols_vectorizer)
        # making predictions
        predictions = self.model.predict(x)
        return ["Spam" if prediction == 1 else "Ham" for prediction in predictions]