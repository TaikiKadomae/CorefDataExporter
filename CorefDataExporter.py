import data
import directories
import TextProcessing
import makeJSON

import os
import random
import pickle

def run(path):

    if path == directories.TRAIN_PATH:
        mode = 'train'
    elif path == directories.DEV_PATH:
        mode = 'dev'
    elif path == directories.TEST_PATH:
        mode = 'test'

    doc = data.Document(path)

    print("mention extracting...")
    paragraphs = doc.paragraphs
    check = paragraphs[0].get_sentences()
    # mention
    if not os.path.exists(directories.PICKLE_PATH + mode + '_mention.pickle'):
        mentions = TextProcessing.mentionExtractor(doc)
        with open(directories.PICKLE_PATH + mode + '_mention.pickle', 'wb') as f:
            pickle.dump(mentions,f)
    else:
        with open(directories.PICKLE_PATH + mode + '_mention.pickle', 'rb') as f:
            mentions = pickle.load(f)

    sep_mentions = TextProcessing.mention_separater(mentions)

    # label feature
    if not os.path.exists(directories.PICKLE_PATH + mode + '_labels.pickle'):
        labels, features, golds = TextProcessing.labelMaker(doc, sep_mentions)
        with open(directories.PICKLE_PATH + mode + '_labels.pickle', 'wb') as f:
            pickle.dump(labels,f)
        with open(directories.PICKLE_PATH + mode + '_features.pickle', 'wb') as f:
            pickle.dump(features,f)
        with open(directories.PICKLE_PATH + mode + '_golds.pickle', 'wb') as f:
            pickle.dump(golds,f)
    else:
        with open(directories.PICKLE_PATH + mode + '_labels.pickle', 'rb') as f:
            labels = pickle.load(f)
        with open(directories.PICKLE_PATH + mode + '_features.pickle','rb') as f:
            features = pickle.load(f)
        with open(directories.PICKLE_PATH + mode + '_golds.pickle','rb') as f:
            golds = pickle.load(f)

    gold = TextProcessing.goldMaker(golds)

    # print('word:{} paras:{} mentions:{} labels:{} features:{}'.format(doc.count_word(),
    #                                                                   len(paragraphs),
    #                                                                   len(mentions),
    #                                                                   len(labels),
    #                                                                   len(features)))

    makeJSON.printer(doc,sep_mentions,labels,features, mode)
    #makeJSON.goldPrinter(gold)
    # target = []
    # for p in doc.paragraphs:
    #     for s in p.sentences:
    #         for ph in s.phrases:
    #             for t in ph.tags:
    #                 target.append(t.get_target())
    #
    # while (True):
    #     try:
    #         target.remove([])
    #     except ValueError:
    #         break
    # new = []
    # for targe in target:
    #     new.append(targe[0])
    # new_target = list(set(new))
    # print(len(new_target))
    # c = 0
    # ex = []
    # for targ in new:
    #     found = False
    #     for m in mentions:
    #         if targ == m.surface:
    #             c = c +1
    #             print(c)
    #             found = True
    #             break
    #     if not found:
    #         ex.append(targ)
    # print(c)
    # print(ex)

if __name__ == '__main__':
    print('making train dataset.')
    run(directories.TRAIN_PATH)
    print('finished.')
    print('making dev dataset.')
    run(directories.DEV_PATH)
    print('finished.')
    print('making test dataset.')
    run(directories.TEST_PATH)
    print('finished.')