import tweepy
import setting
import json
import time

CK = setting.CK
CS = setting.CS
AT = setting.AT
AS = setting.AS

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)
#apiインスタンスを作成
api = tweepy.API(auth)

#調べる単語
keyword = setting.keyword
params = {"q": keyword,'count':5}

search_results = api.search(q=params['q'],count=params['count'])

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id
    user = result.user.name
    tweet = result.text
    time = result.created_at
    print(tweet)
    #リツイートとリプには反応しない
    if 'RT' not in tweet and '@' not in tweet:
        try:
            api.create_favorite(user_id)
            print(user+'をいいねしたんご')
        except:
            print('いいね済みやで')


    print('-'*100)
