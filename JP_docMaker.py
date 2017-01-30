#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

def preprosess(f):
    mention = True
    array = []
    ret = []
    for line in open(f):
        l_array = line.strip().split(' ',3)
        if len(l_array) > 3:
            if l_array[3].startswith('<'):
                print(l_array[3])
        if l_array[0] == '#':
            sent_id = l_array[1].split(':',1)[1]
            doc_id = sent_id.split('-')[0]

        elif l_array[0] == '*':
            phr_id = l_array[1]
            dep = l_array[2].strip()

        elif l_array[0] == '+':
            tag = l_array[1]
            mention = True

        elif l_array[0] == 'EOS' or not mention:
            pass

        else:
            word = l_array[0]
            array = [doc_id,sent_id,phr_id,tag,dep,word]
            #print(array)
            ret.append(array)
            mention = False

    return ret

def make_sentences(f):
    gdoc_id = "ini"
    cng_doc = False
    sent = []
    sentences = []
    ret = []
    for line in f:
        if cng_doc:
            #print(sentences)
            ret.append(sentences)
            sentences = []
            cng_doc = False

        if line[0] == "#":
            doc_id = line[1].rsplit("-",1)[0]
            if gdoc_id == "ini":
                gdoc_id = doc_id
            elif gdoc_id != doc_id:
                gdoc_id = doc_id
                cng_doc = True

        if line[0] not in ["+","*","#"]:
            if line[0] == "EOS":
                sentences.append(sent)
                sent = [] 
                continue
            else:
                    sent.append(line[0])

    return ret


if __name__ == '__main__':
    input_file = '/home/kadomae.13029/kyoto_data/rel/950101.txt'
    preprosess(input_file)
    #make_sentences(array)
    #make_mentions(array)
