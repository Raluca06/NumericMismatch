from nltk.corpus import *
#help(brown)
print reuters.fileids()
print brown.categories()
print brown.fileids(['adventure'])
print brown.categories(['ca01', 'cp28'])
# a = 0
# while (a<=len(brown.words('ca01'))): 
#     brown.words('ca01')[a]
#     a += 1
    
dict={}
for sntc in brown.tagged_sents('ca01'):
        for word,tag in sntc:
            if tag in dict:
                dict[tag]+=1
            else:
                    dict[tag]=1

for tag,count in dict.iteritems():
    if tag=='CD': print tag, count