from textblob import TextBlob
from bs4 import BeautifulSoup
import requests

import sys


def main(URL="https://www.npr.org/2019/12/01/783989343/as-impeachment-inquiry-moves-to-judiciary-committee-republicans-attack-the-proce"):
  r = requests.get(URL)
  soup = BeautifulSoup(r.content, 'html5lib')

  article_text = ''
  article = soup.findAll('p')
  for a in article:
    article_text += a.get_text()

  blob = TextBlob(article_text)
  
  sentences_sentiment = [i.sentiment.polarity for i in blob.sentences]
  print(sum(sentences_sentiment)/len(sentences_sentiment))

if len(sys.argv) > 1:
  main(sys.argv[1])
else:
  main()
