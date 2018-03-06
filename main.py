from polar_dictionary.pol_dict import PolarityDict
import gensim
from preprocess_data.get_data import DataSet
from preprocess_data.feature_extractor import TweetFeatureExtractor
from trainer.trainer import Trainer
from tagger.tagger import SentimentTagger


import pprint
pp = pprint.PrettyPrinter(indent=2, width=200)


def main():
    #get polarity dictionary
    print('Getting polarity dictionary...\n')
    polar = PolarityDict()
    polar.from_file('var/clues.tff.patched')
    print('\nGot polarity dictionary\n')
    print(list(polar.words.items())[:10])
    print("polarities: ", polar.polarities)
    print('part of speech: ', polar.poss)

    word_model = gensim.models.Word2Vec.load('var/my_word_model')

    # get dataset
    train_set = DataSet()
    train_set.from_file('var/train_set.gs')
    pp.pprint(train_set.tweets[:2])

    # get features
    features_list, labels = [], []
    for tweet in train_set.tweets:
        tweet_features = TweetFeatureExtractor(tweet, word_model, polar_dict=polar.words)
        features_list.append(tweet_features.features)
        labels.append(tweet.polarity)

    pp.pprint(features_list[:14])
    pp.pprint(labels[:14])

    # train the crf-trainer
    trainer = Trainer(algorithm=3)
    trainer.feed_trainer(features_list, labels)
    trainer.train('var/')

    # get the test-set
    test_set = DataSet()
    test_set.from_file('var/test_set_dev.gs')
    pp.pprint(test_set.tweets[:2])

    # tag test-set
    tagger = SentimentTagger()
    tagger.load_model('var/sentiment_lbfgs.model')

    tweet_features_list = [TweetFeatureExtractor(tweet, word_model, polar_dict=polar.words).features
        for tweet in test_set.tweets
    ]

    pred_labels = tagger.tag_tweets(tweet_features_list)

    for i, tweet in enumerate(test_set.tweets):
        tweet.polarity = pred_labels[i]

    pp.pprint(test_set.tweets[:2])

    # write output
    with open('var/test_set_dev.pred', mode='w') as out_f:
        out_f.write(str(test_set))


if __name__ == '__main__':
    main()
