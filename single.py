from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

import sys


tb = Blobber()

with open(sys.argv[1], 'r') as f:
  txt = f.read().replace('\n', ' ')

blob = tb(txt)
sentiment = blob.sentiment
print(sys.argv[1], sentiment)
