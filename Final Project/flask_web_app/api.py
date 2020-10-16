import pickle
import pandas as pd

class BookSimilarity(object):
    def __init__(self):
        self.__load_data()

    def __load_data(self):
        self.__book_data = pickle.load(open('data/book_data.pickle', 'rb'))
        print('Loaded book data.')
        self.__cos_sim = pickle.load(open('data/cossim.pickle', 'rb'))
        self.__title_to_idx = pd.Series(self.__book_data.index, index=self.__book_data['title'])
        print('Loaded cosine similarity matrix.')

    def search(self, query):
        return self.__book_data.loc[self.__book_data['title'].str.contains(query, case=False)]

    def recommend(self, title):
        if title not in self.__title_to_idx:
            print('Title not found in index mapping.')
            return None

        book_idx = self.__title_to_idx[title]
        scores = pd.Series(self.__cos_sim[book_idx]).sort_values(ascending=False)
        indices = list(scores.iloc[1:11].index)

        return self.__book_data.iloc[indices]

