from requests_oauthlib import OAuth1Session
import create_sentense
import setting
import json
import time


# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

#ツイート内容
tweet = create_sentense.sentence()

# ツイート本文
params = {"status": tweet}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(setting.CK, setting.CS, setting.AT, setting.AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)

"""
#自分のタイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# 取得数
params = {"count": 5}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(setting.CK, setting.CS, setting.AT, setting.AS)
req = twitter.get(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    timeline = json.loads(req.text)
    for tweet in timeline:
        print(tweet['user']['name']+'::'+tweet['text'])
        print(tweet['created_at'])
        print('-'*30)
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
"""

"""
# キーワードでサーチのURL
url = "https://api.twitter.com/1.1/search/tweets.json"

#調べる単語
keyword = '米谷奈々未'
params = {"q":keyword,"count": 5}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(setting.CK, setting.CS, setting.AT, setting.AS)
req = twitter.get(url, params = params)


# レスポンスを確認
if req.status_code == 200:
    timeline = json.loads(req.text)
    for tweet in timeline['statuses']:
        print(tweet['user']['name']+'::'+tweet['text'])
        print(tweet['created_at'])

        print('-'*100)
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
"""
