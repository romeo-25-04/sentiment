class TweetFeatureExtractor:
    def __init__(self, tweet, training=True):
        self.tweet = tweet
        self.features = self.tweet_features()

    def tweet_features(self):
        nr_tokens = len(self.tweet.tokens)
        return {'stemm': self.tweet.stemms,
                'nr_tokens<5': nr_tokens < 5,
                '5<=nr_tokens<10': 5 <= nr_tokens < 10,
                'nr_tokens>=10': nr_tokens >= 10
                }
