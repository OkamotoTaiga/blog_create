import random

#マルコフ連鎖の辞書を作成関数
def make_dic(words):
    tmp = ['@']
    dic = {}
    for i in words:
        word = i.surface
        if word == '' or word == '\r\n' or word == '\n' or word =='-': continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic,tmp)
        if word == '。':
            tmp = ['top']
            continue
    return dic

#三要素のリストを辞書として登録
def set_word3(dic,s3):
    w1,w2,w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

#文章生成
def make_sentence(dic,member):
    ret = []
    if not 'top' in dic: return 'no dic'
    top = dic['top']
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    while w1 == '。' or w2 == '。':
        w1 = word_choice(top)
        w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        #メンバーに合わせて最後の一行を変える
        if w3 == '。':
            if member=='13':
                ret.append('\n⊿長沢菜々香')
                break
            elif member=='07':
                ret.append('\nsee you again ⊿⊿')
                break
        w1,w2 = w2,w3
    return ''.join(ret)

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys)) #辞書のキーを選ぶ
