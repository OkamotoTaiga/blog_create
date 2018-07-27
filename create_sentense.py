import markov
import json
import random
import setting

members = setting.members
member = random.choice(members)

#辞書の読み込み
markov_dict_file = './dictionary/markov_dic_'+member+'.json'
markov_dic = json.load(open(markov_dict_file,'r'))

#文章生成
def sentence():
    while True:
        s = markov.make_sentence(markov_dic,member)
        if len(s) < 140:
            break
    return s
