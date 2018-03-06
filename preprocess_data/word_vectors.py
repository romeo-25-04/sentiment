from gensim.models import Word2Vec
from preprocess_data.get_data import DataSet

# get dataset
train_set = DataSet()
train_set.from_file('var/train_set.gs')
sentences = [tweet.stemms for tweet in train_set.tweets]
print(sentences[:3])
model = Word2Vec(sentences, min_count=1, hs=1, negative=0,)
model.save('var/my_word_model')
