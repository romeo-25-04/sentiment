from pycrfsuite import Tagger
from pycrfsuite import ItemSequence

class SentimentTagger:
    def __init__(self):
        self.tagger = Tagger()

    def load_model(self, path):
        self.tagger.open(path)

    def tag_tweets(self, tweet_features_list):
        features = ItemSequence(tweet_features_list)
        labels = self.tagger.tag(features)
        return labels
