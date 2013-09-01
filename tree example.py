from nltk.corpus import treebank
from nltk import FreqDist #frequency distance
#help(treebank)
#treebank.fileids()
#print treebank.raw('wsj_0001.mrg')
#a = treebank.raw('wsj_0001.mrg');
a = treebank.tagged_sents('wsj_0001.mrg')[:20].__str__()
print a
fd = FreqDist(a)
print fd['Pierre']
print fd.items()[:30]
#def __init__(self, tree, size):
#uptree.tree 
#self.__dict__.update = nltk.Tree(a)
#print a
#print treebank.tagged_words('wsj_0001.mrg')[:20]
#print treebank.tagged_sents('wsj_0001.mrg')[0]
#print treebank.parsed_sents('wsj_0001.mrg')[0]
print "tree traversal:"
def traverse(t):
    try:
        t.node
    except AttributeError:
        print t,
    else:
        # Now we know that t.node is defined
        print '[', t.node, 
        for child in t:
            traverse(child)
        print ']',
traverse(a)

