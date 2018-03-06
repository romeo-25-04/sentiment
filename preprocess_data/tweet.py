import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

class Tweet:
    def __init__(self, line):
        id1, id2, polarity, text = line.strip().split('\t')
        self.id1 = id1
        self.id2 = id2
        self.polarity = polarity
        self.text = text
        self.tokens = self.clean_tokens()
        ps = PorterStemmer()
        self.stemms = [ps.stem(word) for word in self.tokens]
        self.stemms_bigrams = nltk.bigrams(self.stemms)


    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(
            self.id1,
            self.id2,
            self.polarity,
            self.text
        )

    def clean_tokens(self):
        stopWords = set(stopwords.words('english'))
        tokens = [token for token in nltk.word_tokenize(self.text) if token not in stopWords]
        tokens = [token for token in tokens if '@' not in token]
        return tokens
