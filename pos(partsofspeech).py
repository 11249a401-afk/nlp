import nltk
from nltk.tokenize import word_tokenize
se=input("Enter a sentance:")
words=word_tokenize(se)
pos_tags=nltk.pos_tag(words)
print("words\t\tPOS_TAG")
print("-"*32)
for w,tag in pos_tags:
    print(f"{w}\t|\t{tag}")
    
