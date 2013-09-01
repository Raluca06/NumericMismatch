import nltk, hashlib
import numericMismatch
from nltk.corpus import *
from my_test import sentence

#chunks of type verb "to" verb (ex. want to buy, refuses to continue
# cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
# brown = nltk.corpus.brown
# for sent in brown.tagged_sents():
#     tree = cp.parse(sent)
#     for subtree in tree.subtrees():
#         if subtree.node == 'CHUNK': print subtree
        
#reading IOB Format and the CoNLL 2000 corpus
# print conll2000.chunked_sents('train.txt')[99]
# #select only a certain type of chunk - NP Chunk
# print conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99]
# #evaluate a naive regular expression chunker
# test_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
# grammar = "NP: {<[CDJNP].*>+}"
# cp = nltk.RegexpParser(grammar)
# print cp.evaluate(test_sents)



#training classifier-based chunkers
class ConsecutiveNPChunkTagger(nltk.TaggerI):
    
    def __init__(self, train_sents):
        train_set=[]
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train(train_set, algorithm='megam', trace=0)
    
    def tag(selfself, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self. classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)
    
class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(selfself, train_sents):
        tagged_sents = [[((w,t),c) for (w,t,c) in nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)
        
    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)
    
def npchunk_features(sentence, i, history):
    word, pos = sentence[i]
    return {"pos": pos}
chunker = ConsecutiveNPChunker(train_sents)
print chunker.evaluate(test_sents)