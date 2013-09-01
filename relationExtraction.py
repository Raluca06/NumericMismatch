import nltk, hashlib
import numericMismatch
from nltk.corpus import *

sent = nltk.corpus.treebank.tagged_sents()[22]
sentence4 = "In the latest attacks, two people died and five were severely injured"
sentence = "President Obama has forcibly landed his Air Force One to LAX airport today, while being late to deliver his speech to the Medicare Center, Los Angeles"

tagged = numericMismatch.posTag(sentence)
# print "This is NE chunking:"
# print nltk.ne_chunk(tagged, binary=True)
# print "This is without NE:"
# print nltk.ne_chunk(tagged)

#relation extraction
IN = re.compile('.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG','LOC', doc, corpus='ieer',pattern=IN):
        print nltk.sem.show_raw_rtuple(rel)
# not working

#conll method
vnv = """
    (
    is/V|
    was/V|
    werd/V|
    wordt/V|
    )
    .*
    van/Prep
    """
VAN = re.compile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc, 
                                   corpus='conll2002', pattern=VAN):
        print nltk.sem.show_clause(r, relsym="VAN")

