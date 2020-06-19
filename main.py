# https://repl.it/@JosephVossler/
#
# https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/
# https://www.google.com/search?q=python%20index%20lines%20variable&cad=h
# https://www.google.com/search?q=bs.BeautifulSoup(raw_html,%20%27lxml%27&cad=h
# https://stackabuse.com/read-a-file-line-by-line-in-python/
# https://docs.python.org/3/library/pwd.html
# https://github.com/jvossler/Python_html_Word_Count
# https://stackoverflow.com/questions/860140/whoami-in-python
# https://www.learnpython.org/en/Loops
# https://www.w3schools.com/python/python_variables.asp
# https://www.google.com/search?q=python%20for%20loop%20tutorial&cad=h
# 

import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re
import lxml.html.soupparser
import nltk
nltk.download('punkt')

raw_html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')

article_paragraphs = article_html.find_all('p')

article_text = ''

for para in article_paragraphs:
  article_text += para.text

corpus = nltk.sent_tokenize(article_text)

for i in range(len(corpus )):
  corpus [i] = corpus [i].lower()
  corpus [i] = re.sub(r'\W',' ',corpus [i])
  corpus [i] = re.sub(r'\s+',' ',corpus [i])
print(len(corpus))
print(corpus[30])



#def main():
#   filepath = sys.argv[1]
#
#   if not os.path.isfile(filepath):
#       print("File path {} does not exist. Exiting...".format(filepath))
#       sys.exit()
#  
#   bag_of_words = {}
#   with open(filepath) as fp:
#       cnt = 0
#       for line in fp:
#           print("line {} contents {}".format(cnt, line))
#           record_word_cnt(line.strip().split(' '), bag_of_words)
#           cnt += 1
#   sorted_words = order_bag_of_words(bag_of_words, desc=True)
#   print("Most frequent 10 words {}".format(sorted_words[:10]))
#  
#def order_bag_of_words(bag_of_words, desc=False):
#   words = [(word, cnt) for word, cnt in bag_of_words.items()]
#   return sorted(words, key=lambda x: x[1], reverse=desc)
#
#def record_word_cnt(words, bag_of_words):
#    for word in words:
#        if word != '':
#            if word.lower() in bag_of_words:
#                bag_of_words[word.lower()] += 1
#            else:
#                bag_of_words[word.lower()] = 1
#
#if __name__ == '__main__':
#    main()