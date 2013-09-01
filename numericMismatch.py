import nltk, hashlib
from nltk.corpus import *
from nltk import grammar, chunk

class stru:
    def __init__(self):
            self.key = None
            self.children = []
            self.parent = None
            self.size = 0
            self.tree = None
            self.hash = 0
s = stru()

sentence1 = "Three people were injured"
sentence2 = "In the latest attacks, five people were injured"
sentence3 = "In the latest attacks, five people were injured and two died"
sentence4 = "In the latest attacks, two people died and five were severely injured"
test_sentence = "Pierre Vinken, 61 years old, will join the board as a nonexecutive director Nov. 29."
entities = None
tree = None
ex = treebank.parsed_sents('wsj_0001.mrg')[0]

def posTag(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged

def chunking(tagged_sentence):
    grammar1 = "NP: {<DT|PP\$>?<JJ>*<NN|NNS>}"
    cp = nltk.RegexpParser(grammar1)
    result = cp.parse(tagged_sentence)
    return result

def treefication():
    tree1 = nltk.Tree('NP',['Three'])
    tree2 = nltk.Tree('VP', ['injured'])
    tree3 = nltk.Tree('S',[tree1,tree2])
    return tree3

def printTest(tree3):
    print tree3
    print tree3[1].leaves()
    print tree3[1][len(tree3[1])-1]

def traverse(t):
    try:
        # here are the terminals/leaves
        t.node
    except AttributeError:
#         hash.update()
         print t, len(t[0]),
#         hash.hexdigest()
    else:
        # Now we know that t.node is defined
        # nonterminals
#         hash.update(t.node)
#         if t.node == 'CD':
#             numeral = t.leaves() 
#             numeral[0] = '30'
        print '[', t.node, t.leaves(),
#         hash.hexdigest()
    for child in t:
        traverse(child)
        print ']',
# traverse(result)

tagged1 = posTag(sentence2)
tagged2 = posTag(sentence3)
res1 = chunking(tagged1)
res2 = chunking(tagged2)
print tagged2
#in chunked1
# for word, tag in res1:
#     if tag=='CD': print word
# #in chunked2
# for word, tag in res2:
#     if tag=='CD': print word
#print treefication() 
hash = hashlib.sha1()   
