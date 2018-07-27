from janome.tokenizer import Tokenizer
import json
import markov
import setting

member = setting.member

texts = open('./text/blog_'+member+'.txt','rb').read()
texts = texts.decode()

#形態素解析で名詞の辞書作成
t = Tokenizer()
word_dict_file = './dictionary/word_dic_'+member+'.json'
word_dic = {}
for text in texts:
    words = t.tokenize(text)
    for w in words:
        word = w.surface #単語抽出
        ps = w.part_of_speech #品詞抽出
        if ps.find('名詞') < 0 or word == 'ー': continue
        if not word in word_dic:
            word_dic[word] = 0
        word_dic[word] += 1 #count
    json.dump(word_dic,open(word_dict_file,'w',encoding='utf-8'))

#マルコフ連鎖の辞書を作成
markov_dict_file = './dictionary/markov_dic_'+member+'.json'
#形態素解析
t = Tokenizer()
words = t.tokenize(texts)
#辞書を生成
dic = markov.make_dic(words)
json.dump(dic,open(markov_dict_file,'w',encoding='utf-8'))
