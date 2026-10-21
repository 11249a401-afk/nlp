from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
a=set(stopwords.words("english"))
text="More than 4,500 Google employees have signed a petition asking CEO Sundar Pichai "
t=word_tokenize(text)
l=[]
for i in t:
    if i not in a :
        l.append(i)
print(l)
