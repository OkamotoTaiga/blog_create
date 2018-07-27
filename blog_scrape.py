#モジュール
import urllib.request as req
from bs4 import BeautifulSoup
import setting


#基となるURL
base_url = 'http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&page={page}&cd=member&ct={member}'

member = setting.member #解析したいメンバー

fname = './text/blog_'+member+'.txt' #テキストファイル名
texts = []

for page in range(46):
    #urlopen()でデータ取得
    res = req.urlopen(base_url.format(page=page,member=member))
    #BeautifulSoupで解析
    soup = BeautifulSoup(res,'html.parser')
    #divを取得
    li_list = soup.find_all('div')
    #文字だけ抜き出す
    for i in li_list:
        if not i.string == None and not i.string == '\n' and not i.string == '- - -':
            texts.append(i.string)
            #ファイルへの書き込み
            with open(fname,'a',encoding='utf-8') as f:
                f.write(i.string)
    break
