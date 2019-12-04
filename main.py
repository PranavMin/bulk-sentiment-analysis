from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

import sys
import os
import csv

tb = Blobber()

# Create output folder for CSVs
output_folder = 'output/'
os.mkdir(output_folder)

# Create CSV writer for overall data
out_csv = open(output_folder + 'output_data.csv', 'w')
csv_writer = csv.writer(out_csv)
csv_writer.writerow(['filename', 'polarity', 'subjectivity'])



if len(sys.argv) < 2:
  directory = 'files/'
else:
  directory = sys.argv[1]

for fname in os.listdir(directory):
  with open(directory + fname.strip(), 'r') as f:

    # Clean up newlines and read contents to txt
    txt = f.read().replace('\n', ' ')
    blob = tb(txt)
    
    # Write overall sentiment to csv
    sentiment = blob.sentiment
    csv_writer.writerow([fname.strip(), sentiment.polarity, sentiment.subjectivity])
    
    # Write individual sentence sentiment to individual files
    indiv_out_csv = open(output_folder + fname[:-3]+'csv', 'w')
    indiv_csv_writer = csv.writer(indiv_out_csv)
    
    for sentence in blob.sentences:
      indiv_csv_writer.writerow([sentence.sentiment.polarity, sentence])
    indiv_out_csv.close()

    print(fname.strip(), sentiment)

out_csv.close()
