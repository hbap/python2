import nltk
import os
import sys


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self):
        """Initialize Analyzer."""

        # instantiate tokenizer
        self.tokenizer = nltk.tokenize.TweetTokenizer()

        # load positive words
        self.positives = set()
        with open(os.path.join(sys.path[0], "positive-words.txt")) as lines:
            for line in lines:
                line = line.strip()
                if line and not line.startswith(";"):
                    self.positives.add(line)

        # load negative words
        self.negatives = set()
        with open(os.path.join(sys.path[0], "negative-words.txt")) as lines:
            for line in lines:
                line = line.strip()
                if line and not line.startswith(";"):
                    self.negatives.add(line)

    def analyze(self, text):
        """Analyze text for sentiment, returning a score."""

        # tokenize text
        tokens = self.tokenizer.tokenize(text)

        # score text
        score = 0
        for token in tokens:
            token = token.lower()
            if token in self.positives:
                score += 1
            if token in self.negatives:
                score -= 1
        return score
