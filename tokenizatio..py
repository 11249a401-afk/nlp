from nltk.tokenize import sent_tokenize,word_tokenize
a="This is nlp lab. We are doing program "
print(word_tokenize(a))
for i in word_tokenize(a):
    print(i)
print(sent_tokenize(a))
for i in sent_tokenize(a):
    print(i)
