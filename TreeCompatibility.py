from nltk.corpus import *
# from nltk.book import *
import hashlib

class stru:
    def __init__(self):
            self.key = None
            self.left = None
            self.right = None
            self.size = 0
            self.tree = treebank.parsed_sents('wsj_0001.mrg')[0]
s = stru()

a = treebank.raw('wsj_0001.mrg')
b = treebank.tagged_sents('wsj_0001.mrg')
f = open('workfile','w')
# print type(a)
# print type(b)
# print s.tree
# print s.tree.leaves()

# print s.tree
#print s.tree
hash = hashlib.sha1()
def traverse(t):
    try:
        #here are the terminals/leaves
        t.node
    except AttributeError:
        hash.update(t)
        print t, len(t[0]), hash.hexdigest()
    else:
        # Now we know that t.node is defined
        #nonterminals
        hash.update(t.node)
        print '[', t.node, len(t), hash.hexdigest()
        for child in t:
            traverse(child)
        print ']',
#traverse(s.tree)

# text1.dispersion_plot(['monstrous'])
# print text1.similar('captain')

for ch_tree in s.tree:
    if (ch_tree.node.startswith('JJ')):
        print ch_tree.leaves()