from textblob import TextBlob
from bs4 import BeautifulSoup
import requests



#https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558


def main():
  URL = "https://www.npr.org/2019/12/01/783989343/as-impeachment-inquiry-moves-to-judiciary-committee-republicans-attack-the-proce"
  r = requests.get(URL)
  soup = BeautifulSoup(r.content, 'html5lib')

  article_text = ''
  article = soup.findAll('p')
  for a in article:
    article_text += a.get_text()

  print(article_text)

  blob = TextBlob(article_text)
  for sentence in blob.sentences:
    print(sentence.sentiment.polarity)

main()
