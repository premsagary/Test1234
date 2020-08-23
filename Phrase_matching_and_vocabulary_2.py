import spacy 
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

with open('reaganomics.txt') as f:
    doc3 = nlp(f.read())

phrase_list = ['vooodoo economics', 'supply-side economics', 'trickle-down economics', 'free-market economics']

phrase_patterns = [nlp(text) for text in phrase_list]
matcher.add('EconMatcher', None, *phrase_patterns)


found_matches = matcher(doc3)
print(found_matches)