import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
import string
t=input("enter text:")
l=t.lower()
tokens=word_tokenize(l)
token=[word for word in tokens if word not in string.punctuation]
stop=set(stopwords.words('english'))
filt=[word for word in token if word not in stop]
ps=PorterStemmer()
st_words=[ps.stem(word) for word in filt]
frequency=Counter(filt)
print("\nOriginal Tokens:")
print(token)
print("\nFilter Words:")
print(filt)
print("\nStemmed Words:")
print(st_words)
print("\nword frequency:")
for word,count in frequency.items():
    print(word,":",count)
    
