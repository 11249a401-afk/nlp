from nltk.stem import PorterStemmer
p=PorterStemmer()
words=["running","lovely","connection","died"]
for w in words:
    print(p.stem(w))
