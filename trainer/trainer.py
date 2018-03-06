from pycrfsuite import ItemSequence
from pycrfsuite import BaseTrainer


class Trainer:
    ALGORITHMS = [
        'lbfgs',    # 0 for Gradient descent using the L-BFGS method, BEST
        'l2sgd',    # 1 for Stochastic Gradient Descent with L2 regularization term
        'ap',       # 2 for Averaged Perceptron
        'pa',       # 3 for Passive Aggressive
        'arow'      # 4 for Adaptive Regularization Of Weight Vector
    ]

    def __init__(self, algorithm=0, iterations=50):
        self.algorithm = self.ALGORITHMS[algorithm] if algorithm in range(5) else self.ALGORITHMS[4]
        self.trainer = BaseTrainer(algorithm=self.algorithm)
        self.trainer.set('max_iterations', iterations)

    def feed_trainer(self, features_list, labels):
        features = ItemSequence(features_list)
        self.trainer.append(features, labels)

    def train(self, path='var/'):
        self.trainer.train(path+'/sentiment_'+self.algorithm+'.model')
