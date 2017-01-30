import pickle
import random


with open('/home/kadomae.13029/work/data/pickle/paragraphs.pickle', 'rb') as para:
    p = pickle.load(para)

train = open('train.txt','w')
dev = open('dev.txt','w')
test = open('test.txt','w')

random.shuffle(p)

train_a = p[0:300]
dev_a = p[300:400]
test_a = p[400:]

for tr in train_a:
    for tl in tr:
        train.write(tl)

for dl in dev_a:
    for de in dl:
        dev.write(de)

for tel in test_a:
    for tes in tel:
        test.write(tes)

train.close()
dev.close()
test.close()