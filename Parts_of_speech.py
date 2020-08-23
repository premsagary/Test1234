import spacy 
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"The quick brown fox jumped over the lazy dogs's back.")
for token in doc:
    print(f"{token.text:->{10}} {token.pos_:->{10}} {token.dep_:->{10}} {token.tag_:->{10}} {spacy.explain(token.tag_):->{10}}") #"tag_" find grade tag
    #spacy.explain can explain anything pos,dep


