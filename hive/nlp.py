from flair.models import TextClassifier
from flair.data import Sentence


classifier = TextClassifier.load('en-sentiment')


class NLP(object):

    @staticmethod
    def analyzeSentiment(message):
        sentence = Sentence(message)
        classifier.predict(sentence)
        return sentence.labels
