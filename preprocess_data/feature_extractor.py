class TweetFeatureExtractor:
    NEGATIONS = ["n't", 'not']

    def __init__(self, tweet, word_model, polar_dict=dict(), training=True):
        self.tweet = tweet
        self.polar_dict = polar_dict
        self.word_model = word_model
        self.features = self.tweet_features()

    def tweet_features(self):
        nr_tokens = len(self.tweet.tokens)
        polarities = [self.polar_dict.get(stemm, 'neutral') for stemm in self.tweet.stemms]
        return {
            'stemm_vectors': [self.word_model.wv[stemm]
                              for stemm in self.tweet.stemms],
            'stemm_score': self.word_model.score([self.tweet.stemms]).sum(),
            'positive': len([pol for pol in polarities if pol == 'positive']),
            'negative': len([pol for pol in polarities if pol == 'negative']),
            'neutral': len([pol for pol in polarities if pol == 'neutral']),
            'nr_tokens<5': nr_tokens < 5,
            '5<=nr_tokens<10': 5 <= nr_tokens < 10,
            'nr_tokens>=10': nr_tokens >= 10
        }
