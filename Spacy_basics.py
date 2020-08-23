import spacy
nlp = spacy.load('en_core_web_sm') #loadig a model and stored it in "nlp" variable
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')
for token in doc:
    print(token.text, token.pos_, token.dep_)  #pos - Parts of speach, #dep - syntactic dependency, .txt- is just text form
    # "_" after the pos and dep give the names instead of numbers
print(nlp.pipeline)  #Spacy contains series of pipelines, you can use this to see pipelines
print(nlp.pipe_names) #you can use this to get list of pipeline names



#Tokenization
# Tokenization is splitting up all the components words, punchuation into tokens. Tokens are annotated into a doc
doc2 = nlp(u"Tesla isn't looking into startups anymore.")
for token in doc2:
    print(token.text, token.pos_, token.dep_)
print(doc2[0].pos_) #Prints parts of speech for token in doc2[0]
print(doc2[0].dep_) #Prints syntactic dependency for token in doc2[0]


doc3 = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
the phrase "Life is what happens to us while we are making other plans" was written by \
cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')

life_quote = doc3[16:30]
print(life_quote)
print(type(life_quote))
print(type(doc3))

doc4 = nlp("this is a first sentence. This is a second sentence. This is a third sentence")
for sentence in doc4.sents:
    print(sentence)

print(doc4[6].is_sent_start) #Is it the start of a sentence
print(doc4[8].is_sent_start)


#Tokenization

#Prefix Charecters at the beginning  ($ " ')
#Suffix characters at the end (km , ) . !)
#Infix Characters in between (let's U.S.)
#Exception special-case rule to split a string into several tokens or prevent a token from being splitwhen punchuation rules are applied.

mystring = ' "We\'re moving to L.A.!"'
print(mystring)
doc5 = nlp(mystring)
for token in doc5:
    print(token.text)

doc6 = nlp(u"We're here to help! send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")
for token in doc6:
    print(token)


doc7 = nlp(u"A 5km NYC cab ride costs $10.30")
for token in doc7:
    print(token)

doc8 = nlp(u"Let's visit St. Louis in the U.S. next year.")
for token in doc8:
    print(token)

print(len(doc7))

print(len(doc4.vocab)) #Shows the total nnumber of vocablary in the loaded model

doc9 = nlp(u"It is better to give than receive")
print(doc9[0])
print(doc9[2:5])


doc10 = nlp(u"Apple to build a Hong Kong factory for $6 million")
for token in doc10:
    print(token.text, end='|')
for entity in doc10.ents:                                       #Spacy can identify entity
    print(entity)
    print(entity.label_)                                         #It can attach labels
    print(str(spacy.explain(entity.label_)))                      #It can attach explain labels for entity                                       
    print('\n')

doc11 = nlp(u"Autonomous cars shift insurance liability towards maufacturers")
for chunk in doc11.noun_chunks:                                 #prints nowns and discribing that nouns
    print(chunk)


""" Token.text    #words
token.pos_    #Parts of speech
token.dep_    #syntactic dependency
nlp.pipeline    #pipeline in spacy
nlp.pipeline.names  #names of pipeline in spacy
doc4.sents          #Prints sentences
doc4[6].is_sent_start #is that word at the starting of the sentence? #True or  #None
doc10.ents          #Prints entities
entity.label_       #Labels entities
spacy.explain(entity.label_)  #Expains the lables of entities
doc11.noun_chunks       #Prints the nowns and discription of that nowns in the doc """

