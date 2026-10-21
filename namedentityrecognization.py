import spacy
nlp = spacy.load("en_core_web_sm")
text=input("enter text:")
d=nlp(text)
print("\n named entities")
print("-"*40)
for ent in d.ents:
    print(f"Entity:{ent.text}")
    print(f"Lable:{ent.label_}")
    print("meaning:",spacy.explain(ent.lable_))
    print("-"*40)
    
