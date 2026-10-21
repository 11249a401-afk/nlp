import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams as grams
text = input("Enter a sentence: ")
tokens = word_tokenize(text)
print("\nOriginal Tokens")
print(tokens)
print("\nUnigrams")
for gram in grams(tokens, 1):
    print(gram)
print("\nBigrams")
for gram in grams(tokens, 2):
    print(gram)
print("\nTrigrams")
for gram in grams(tokens, 3):
    print(gram)
