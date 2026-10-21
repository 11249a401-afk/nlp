import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
text = input("Enter a sentence: ")
tokens = word_tokenize(text)
tags = pos_tag(tokens)
print("\nPOS Tags using Viterbi Decoding Concept")
print("-" * 45)
for word, tag in tags:
 print(f"{word:<15} {tag}") 
