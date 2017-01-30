import json
import collections

def printer(doc, mentions, labels, features, mode):
    feature_names = ["same-speaker",
                     "antecedent-is-mention-speaker",
                     "mention-is-antecedent-speaker",
                     "relaxed-head-match",
                     "exact-string-match",
                     "relaxed-string-match"]
    file = open(mode, 'w')
    for p, m, l, f in zip(doc.paragraphs, mentions, labels, features):
        arr_sentences = p.get_sentences()
        dic_mentions = collections.OrderedDict()
        dic_labels = collections.OrderedDict()
        dic_pair_features = collections.OrderedDict()
        dic_document_features = collections.OrderedDict()
        dic_doc = collections.OrderedDict()

        #sentence
        dic_doc['sentences'] = arr_sentences
        #mentions
        for each_m in m:
            dic_m = collections.OrderedDict()
            dic_m['doc_id'] = each_m.doc_id
            dic_m['mention_id'] = each_m.mention_id
            dic_m['mention_num'] = each_m.mention_num
            dic_m['sent_num'] = each_m.sent_num
            dic_m['start_index'] = each_m.start_index
            dic_m['end_index'] = each_m.end_index
            dic_m['head_index'] = each_m.head_index
            dic_m['mention_type'] = each_m.mention_type
            dic_m['dep_relation'] = each_m.dep_relation
            dic_m['dep_parent'] = each_m.dep_parent
            dic_m['sentence'] = each_m.sentence
            dic_m['contained-in-other-mention'] = each_m.contained_in_other_mention
            dic_mentions[each_m.mention_id] = dic_m
        dic_doc['mentions'] = dic_mentions
        #labels
        for each_l in l:
            dic_labels[each_l[0]] = each_l[1]
        dic_doc['labels'] = dic_labels
        #pair-feature-name
        dic_doc['pair_feature_names'] = feature_names
        #pair-feature
        for each_f in f:
            feature = [each_f[1].same_speaker,
                       each_f[1].antecedent_is_mention_speaker,
                       each_f[1].mention_is_antecedent_speaker,
                       each_f[1].relaxed_head_match,
                       each_f[1].exact_string_match,
                       each_f[1].relaxed_string_match]
            dic_pair_features[each_f[0]] = feature
        dic_doc['pair_features'] = dic_pair_features
        #document_feature
        dic_document_features['doc_id'] = p.paragraph_id
        dic_document_features['type'] = 0
        dic_document_features['source'] = "bc"
        dic_doc["document_features"] = dic_document_features
        ppp = json.dumps(dic_doc, ensure_ascii=False)

        file.write(ppp)
        file.write('\n')
    file.close()

def _printer(doc, mentions, labels, features):
    for p, m, l, f in zip(doc.paragraphs, mentions, labels, features):
        print('{"sentences":' + str(p.get_sentences()),end=',')
        print('"mentions":{',end='')
        for each_m in m:
            print('"' + str(each_m.mention_id) + '":{' +
                  '"doc_id":' + str(each_m.doc_id) + ','
                  '"mention_id":' + str(each_m.mention_id) + ','
                  '"mention_num":' + str(each_m.mention_num) + ','
                  '"sent_num":' + str(each_m.sent_num) + ','
                  '"start_index":' +str(each_m.start_index) + ','
                  '"end_index":' + str(each_m.end_index) + ','
                  '"head_index":' + str(each_m.head_index) + ','
                  '"mention_type":"' + str(each_m.mention_type) + '",'
                  '"dep_relation":"' + str(each_m.dep_relation) + '",'
                  '"dep_parent":"' + str(each_m.dep_parent) + '",'
                  '"sentence":' + str(each_m.sentence) + ','
                  '"contained_in_other_mention":' + str(each_m.contained_in_other_mention) + '}',end='')
        print('}',end=',')
        print('"labels":{',end='')
        i = 0
        for each_l in l:
            print('"' + str(each_l[0]) + '":' + str(each_l[1]), end='')
            if not i == len(l):
                print(',',end='')
            i = i + 1
        print('},',end='')
        print('"pair_feature_names":' + str(feature_names),end='')
        print('"pair_features":{',end='')
        k = 0
        for each_f in f:
            print('"' + str(each_f[0]) + '":[' +
                  str(each_f[1].same_speaker) + ',' +
                  str(each_f[1].antecedent_is_mention_speaker) + ',' +
                  str(each_f[1].mention_is_antecedent_speaker) + ',' +
                  str(each_f[1].relaxed_head_match) + ',' +
                  str(each_f[1].exact_string_match) + ',' +
                  str(each_f[1].relaxed_string_match) + ']',end='')
            if not k == len(f):
                print(',',end='')
            k = k + 1
        print('},',end='')
        print('"document_features":{"doc_id":' + str(p.paragraph_id) +
              ',"type":0,"source":"bc"}',end='')
        print('}')

def goldPrinter(gold):
    i = 0
    for g in gold:
        print('{"' + str(i) + '":' + str(g) + '}')
        i = i + 1
