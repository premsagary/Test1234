# Lemmatization is much more informative than Stemming, this is why spacy has only Lemmatization not stemming
#It will look surrounding text to determine the parts of speech

import spacy
nlp = spacy.load('en_core_web_sm')

doc1 = nlp(u"I am a runner running a race because I love run since I ran today")
for token in doc1:
    print(f"{token.text:{15}} {token.pos_:->{15}} {token.lemma:->{22}} {token.lemma_:->{15}}") #'\t' you can use for tab(space)
    #.lemma gives hash value

""" 
output:

I               -----------PRON ----561228191312463089 ----------PRON-
am              ------------AUX --10382539506755952630 -------------be
a               ------------DET --11901859001352538922 --------------a
runner          -----------NOUN --12640964157389618806 ---------runner
running         -----------VERB --12767647472892411841 ------------run
a               ------------DET --11901859001352538922 --------------a
race            -----------NOUN ---8048469955494714898 -----------race
because         ----------SCONJ --16950148841647037698 --------because
I               -----------PRON ----561228191312463089 ----------PRON-
love            -----------VERB ---3702023516439754181 -----------love
run             -----------NOUN --12767647472892411841 ------------run
since           ----------SCONJ --10066841407251338481 ----------since
I               -----------PRON ----561228191312463089 ----------PRON-
ran             -----------VERB --12767647472892411841 ------------run
today           -----------NOUN --11042482332948150395 ----------today

 """
