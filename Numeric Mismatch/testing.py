import nltk, hashlib

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