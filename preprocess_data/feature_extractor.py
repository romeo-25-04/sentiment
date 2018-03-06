class TweetFeatureExtractor:
    NEGATIONS = ["n't", 'not']
    POS_EMOTES = [(':', ')')]
    NEG_EMOTES = [(':', '(')]

    def __init__(self, tweet, word_model, polar_dict=dict(), training=True):
        self.tweet = tweet
        self.polar_dict = polar_dict
        self.word_model = word_model
        self.features = self.tweet_features()

    def tweet_features(self):
        nr_tokens = len(self.tweet.tokens)
        polarities = [self.polar_dict.get(stemm, 'neutral') for stemm in self.tweet.stemms]
        max_polar = dict()
        for item in polarities:
            if item != 'neutral':
                val = max_polar.get(item, 0) + 1
                max_polar[item] = val

        features = {
            'stemms': self.tweet.stemms,
            'max_pol': max(max_polar, key=lambda key: max_polar[key]),
            'positive': len([pol for pol in polarities if pol == 'positive']),
            'negative': len([pol for pol in polarities if pol == 'negative']),
            'neutral': len([pol for pol in polarities if pol == 'neutral']),
            'nr_tokens<5': nr_tokens < 5,
            '5<=nr_tokens<10': 5 <= nr_tokens < 10,
            'nr_tokens>=10': nr_tokens >= 10,
            'negation_in_tweet': self.negation_in_tweet(),
            'pos_emotes_in': self.pos_emotes_in(),
            'neg_emotes_in': self.neg_emotes_in()

        }
        scores = self.get_scores()
        features.update(scores)
        return features

    def get_scores(self):
        vocab = list(self.word_model.wv.vocab)
        scores = []
        for i, stemm in enumerate(self.tweet.stemms):
            if stemm in vocab:
                score = self.word_model.wv[stemm].sum()
            else:
                score = 1
            scores.append((stemm, score))
        return dict(scores)

    def negation_in_tweet(self):
        for negation in self.NEGATIONS:
            return negation in self.tweet.stemms
        return False

    def pos_emotes_in(self):
        for emote in self.POS_EMOTES:
            return emote in self.tweet.stemms_bigrams
        return False

    def neg_emotes_in(self):
        for emote in self.NEG_EMOTES:
            return emote in self.tweet.stemms_bigrams
        return False
