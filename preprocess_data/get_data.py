from preprocess_data.tweet import Tweet


class DataSet:
    def __init__(self):
        self.tweets = []

    def from_file(self, path):
        with open(path) as f:
            self.tweets = [
                Tweet(line)
                for line in f
            ]

    def from_string(self, line_str):
        self.tweets.append(Tweet(line_str))

    def __add__(self, other):
        new_data = DataSet()
        new_data.tweets = self.tweets + other.tweets
        return new_data

    def __repr__(self):
        return '\n'.join(str(tweet) for tweet in self.tweets)
