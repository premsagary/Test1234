import spacy
nlp = spacy.load("en_core_web_sm")
print(len(nlp.vocab))  # 489
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
print(len(matcher))   # 0 

# Check the jupiter book of udemy for more patterns
#SolarPower
pattern1 = [{'LOWER':'solarpower'}]
#Solar-Power
pattern2 = [{'LOWER':'solar'}, {'IS_PUNCT':True},{'LOWER':'power'}]
#Solar power
pattern3 = [{'LOWER':'solar'},{'LOWER':'power'}] 


matcher.add('SolarPower', None, pattern1,pattern2,pattern3)  # Adding word and patterns to the matcher library

print(len(matcher))  # 1

doc=nlp(u"The Solar Power industry continues to grow a solarpower increases. Solar-power is amazing")


found_matches = matcher(doc) 
print(found_matches)

for match_id, start,end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)

matcher.remove('SolarPower')


#solarPower, SolarPower
pattern1 = [{'LOWER':'solarpower'}]

#solar.power
pattern2 = [{'LOWER':'solar'}, {'IS_PUNCT':True,'OP':'*'}, {'LOWER':'power'} ] # "*" allows pattern to match zero or more times
matcher.add('SolarPower', None, pattern1,pattern2)

doc2 = nlp(u"Solar--power is solarpower yay!")
found_matches = matcher(doc2) 
print(found_matches)

for match_id, start,end in found_matches:
    string_id = nlp.vocab.strings[match_id]
    span = doc2[start:end]
    print(match_id, string_id, start, end, span.text)