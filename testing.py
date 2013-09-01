import nltk, hashlib
from nltk.corpus import wordnet as wn
sentences = []
f = open('input(2).txt')
g = open('results.txt', 'w')
sentenceTemp = ''
for line in f:
    if (line == '#\n'):
        sentences.append(sentenceTemp)
        sentenceTemp = ''
    else: sentenceTemp = sentenceTemp + line

print len(sentences)

c = 0
for i in range(0, len(sentences)-1, 2):
    print i, i+1
    tempTree = nltk.tree.Tree(sentences[i])
    tempTree2 = nltk.tree.Tree(sentences[i+1])
    prod1 = tempTree.productions()
    prod2 = tempTree2.productions()
    subtrees1 = []
    for i in range(tempTree.height()):
            for s in tempTree.subtrees(lambda tempTree: tempTree.height() == i):
                        subtrees1.append(s)

    subtrees2 = []
    for i in range(tempTree2.height()):
            for s in tempTree2.subtrees(lambda tempTree2: tempTree2.height() == i):
                        subtrees2.append(s)
                        
    if(subtrees1==subtrees2):
        print 'Sentences match: no contradictions'
    else:
        for i, j in zip(subtrees1, subtrees2):
            if i != j:
                if((i.node=='CD') & (j.node=='CD')):
                    print 'Numeric mismatch:'
                    print i.leaves(), j.leaves(),'\n'
                    c += 1
                    
g.write(c.__str__())
g.close()