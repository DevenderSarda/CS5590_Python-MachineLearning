import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

import re
import urllib.request

def fn_tokens(text):
    return re.findall('[a-z]+', text.lower())

#Reading Text file
with open("inputfile",'r') as f:
    content_input = f.read()

WORDS_input = fn_tokens(open('inputfile').read())
print(WORDS_input)
print(content_input)

#Tokenization
from nltk.stem import WordNetLemmatizer
print("\n")
print("LEMMATIZATION")
lemmatize_list_input = []
lemmatizer=WordNetLemmatizer()
for WORD in WORDS_input:
    print(lemmatizer.lemmatize(WORD))

#Bi-GRAM
from nltk import word_tokenize
from nltk.util import ngrams
print("\n\n")
print("BI-GRAM")
input_list = []
for WORD in WORDS_input:
    input_list=input_list+[WORD]

def fn_find_trigrams(input_list):
  bigram_list_input = []
  for i in range(len(input_list)-2):
      bigram_list_input.append((input_list[i], input_list[i+1]))
  return bigram_list_input
print(fn_find_trigrams(input_list))
print("\n")

#Bi-gram frequency
print("\n")
print("BIGRAM FREQUENCY")
frequencies_counter = Counter([])
bigrams = ngrams(WORDS_input, 2)
frequencies_counter += Counter(bigrams)
print(frequencies_counter)

#Top five bi-gram word
print("\n")
print("TOP FIVE BI-GRAM WORDS")
topFiveBG=list()
for i in range (0,5) :
    topFiveBG.append(" ".join(re.findall("[a-zA-Z]+",str(frequencies_counter).split(":")[i])))
print(topFiveBG)

#Finding all the sentences with those most repeated bi-grams
print("\n")
print("ALL SENTENCE WITH MOST BI-GRAM WORDS")
lines={}
for line in content_input.split("."):
    for word in topFiveBG:
        if word in line:
            if line in lines:
                pass
            else:
                lines[line]=""
result=list()
for line in lines:
    result.append(line+".")
print(result)