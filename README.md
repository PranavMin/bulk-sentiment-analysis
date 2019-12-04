# bulk-sentiment-analysis

A simple tool to run TextBlobs sentiment analysis on a large amount of files and output the data in a csv (filename,polarity,subjectivity) and individual csvs that give the sentiment of each sentence. 

## How to install 
```
git clone https://github.com/PranavMin/bulk-sentiment-analysis.git
cd bulk-sentiment-analysis
pip3 install bs4
pip3 install textblob
python3 -m textblob.download_corpora
```

## How to use
Populate files/ with whatever text files you want to analyze and then run `python3 main.py' and the output will be put in output/
