""" 
Stemming ia a crude of finding the base form of a word
Spacy don't include stemming only does lemmitization


Potter Stemmer and Snowball Stemmer
Potter stemmer :
Potter stemmer is developped by Martin Potter
Potter stemmer have 5 phases (Word -> stem)

Snowball Stemmer:
Snowball Stemmer is also developed by Martin Potter also called English stemmer or Porter2 stemmer

 """

# Potter stemmer :
import nltk     #nltk - natural language toolkit
from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()

words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly']
for word in words:
    print(f"{word:{10}} {p_stemmer.stem(word):->{15}}")


""" 
output:
run        ------------run
runner     ---------runner
ran        ------------ran
runs       ------------run
easily     ---------easili
fairly     ---------fairli

"""

# Snoball stemmer :
import nltk
from nltk.stem.snowball import SnowballStemmer
words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly']
s_stemmer = SnowballStemmer(language='english')
for word in words:
    print(f"{word:{10}} {s_stemmer.stem(word):->{15}}")

""" 
output:
run        ------------run
runner     ---------runner
ran        ------------ran
runs       ------------run
easily     ---------easili
fairly     -----------fair

"""




words = ['generous', 'generation', 'generously','generate']
for word in words:
    print(f"{word:{10}} {p_stemmer.stem(word):->{15}} {s_stemmer.stem(word):->{15}}")


""" 
output:
generous   ----------gener -------generous
generation ----------gener --------generat
generously ----------gener -------generous
generate   ----------gener --------generat

"""

