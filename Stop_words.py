# Stop words are those which don't really give any information like "a", "the"
import spacy
nlp = spacy.load('en_core_web_sm')

print(nlp.Defaults.stop_words)  # Displays all the stop words

print(nlp.vocab['is'].is_stop) #output:True , will give a boolean output if the given word is preset in stop words or not

nlp.Defaults.stop_words.add('btw')     #add "btw" as a stop word
print(nlp.vocab['btw'].is_stop) #output:True , will give a boolean output if the given word is preset in stop words or not


nlp.Defaults.stop_words.remove('almost')  #remove "almost" as a stop word
print(nlp.vocab['almost'].is_stop) #output:False , will give a boolean output if the given word is preset in stop words or not


