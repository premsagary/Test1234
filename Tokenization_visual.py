import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

def write_output(input):
    with open("doc1_display.html", "r") as writer:
        writer.write(input)

doc = nlp(u"Apple is going to build a U.K. factory for $6 million.")
output = displacy.render(doc, style='dep')   #"dep" for syntactic dependency
write_output(output)


doc1 = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million")
output1 = displacy.render(doc1, style='ent')      #"ent" for entity 
write_output(output1)


doc1 = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million")
displacy.serve(doc1,style='ent')                #displays output on the laptop browser, serv is server I guess


# displacy.render(doc, style='dep') #"dep" for syntactic dependency  #render for output in files
# displacy.serve(doc1,style='ent')   #"ent" for entity #serve for displaying output on laptop


