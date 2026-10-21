from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()
print(lem.lemmatize("cats"))
print(lem.lemmatize("cacti"))
print(lem.lemmatize("better",pos='a'))
print(lem.lemmatize("geeses"))
print(lem.lemmatize("rocks"))
print(lem.lemmatize("happy",pos='a'))
