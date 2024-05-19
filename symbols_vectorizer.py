class SymbolsVectorizer:
    def fit(self, ssymbols_lists):
        # сreate a unique list of all special symbols found in the input lists
        self.dictionary = list(set([symbol for sublist in ssymbols_lists for symbol in sublist]))
        # сreate a dictionary that maps each symbol to a unique index
        self.matrix = {symbol: index for index, symbol in enumerate(self.dictionary)}
        # return the instance of the class
        return self
    
    def transform(self, ssymbols_lists):
        # initialize an empty list to hold the vectorized outputs
        vectorized = []
        for sublist in ssymbols_lists:
            # create a vector where each element is related with each unique symbol
            vectorized_sublist = [0] * len(self.dictionary)
            # iterate over each symbol in the sublist
            for symbol in sublist:
                # if the symbol is in the dictionary, increment the corresponding index in the vector
                if symbol in self.dictionary:
                    symbol_idx = self.matrix[symbol]
                    vectorized_sublist[symbol_idx] += 1
            # append the vectorized speacial symbols to the output list
            vectorized.append(vectorized_sublist)
        # return the batch of vectorized special special symbols
        return vectorized

    def fit_transform(self, ssymbols_lists):
        # fit the vectorizer
        self.fit(ssymbols_lists)
        # transform the data using the fitted vectorizer
        vectorized = self.transform(ssymbols_lists)
        # return the transformed data
        return vectorized
