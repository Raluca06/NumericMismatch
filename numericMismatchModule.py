import os, sys
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
another_test = "Carter was the 39th president of the United States."
news = "Non-acceptance would cause embarrassment to donor and U.S. government."
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
# res1 = chunking(tagged1)
# res2 = chunking(tagged2)
print tagged2
numeral1 = ""
numeral2 = ""
#in chunked1
for word, tag in tagged1:
    if tag=='CD': 
        print word
        numeral1 = word
#in chunked2
for word, tag in tagged2:
    if tag=='CD': 
        print word
        numeral2 = word

if (numeral1 != numeral2): 
    print "Mismatch -> possible contradiction"
else: print "No Mismatch"
#print treefication() 
#hash = hashlib.sha1()   
# f = open('input.txt')
# sentences = []
# for line in f:
#     global sentenceTemp 
#     sentenceTemp = ''
#     if line=='(ROOT':
#         if (line[0]in ('(',' ')): sentenceTemp = sentenceTemp + line
#     else: 
#         sentences.append(sentenceTemp)
#         sentenceTemp = ''
#     print line
# print sentences

sentences = []
f = open('test_input.txt')
g = open('results.txt', 'a')
sentenceTemp = ''
for line in f:
    if (line[0] == '\n'):
        sentences.append(sentenceTemp)
        sentenceTemp = ''
    else: sentenceTemp = sentenceTemp + line

print sentences

# for sentence, sentence2 in sentences:
#     tempTree = nltk.tree.Tree(sentence)
#     tempTree2 = nltk.tree.Tree(sentence2)
#     prod1 = tempTree.productions()
#     prod2 = tempTree2.productions()
#     subtrees1 = []
#     for i in range(tempTree.height()):
#             for s in tempTree.subtrees(lambda tempTree: tempTree.height() == i):
#                         subtrees1.append(s)
#     subtrees2 = []
#     for i in range(tempTree2.height()):
#             for s in tempTree2.subtrees(lambda tempTree2: tempTree2.height() == i):
#                         subtrees2.append(s)
#     if(subtrees1==subtrees2):
#         print 'Sentences match: no contradictions'
#     else:
#         for i, j in zip(subtrees1, subtrees2):
#             if i != j:
#                 if(i.node=='CD'):
#                     print 'Numeric mismatch:'
#                     print i.leaves(), j.leaves(),
                    
                    
                    
                    
                    
                    
# g.write(tempTree.leaves())

# f1 = open('input4.txt')
# sentenceTemp = ''
# for line in f1:
#         if (line[0]in ('(',' ')): sentenceTemp = sentenceTemp + line
# 
# #print tempTree2.leaves()




g.close()
