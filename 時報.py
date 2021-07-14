#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリ：tweepy (インストール方法：コマンドプロンプトで 「pip install tweepy」)
import tweepy
import datetime
import time
 
# 取得した各種キーを格納-----------
# Twitter APIを登録すること。
consumer_key ="ここにキーを入れてね。(""は消さないこと。)"         # API key (旧コンシューマーキー)
consumer_secret ="ここにキーを入れてね。(""は消さないこと。)"      # API Secret Key (旧コンシューマーシークレットキー)
access_token="ここにキーを入れてね。(""は消さないこと。)"          # Access Token Key
access_token_secret ="ここにキーを入れてね。(""は消さないこと。)"  # Access Token Secret key


# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#----------------------------------

while True:
    
    # 時刻を取得
    now =datetime.datetime.now()
    clock = (now.strftime('%H:%M'))
    print ("時刻は"+str(clock)+"をお知らせいたします。")

    # ツイートを投稿
    api.update_status("時刻は"+str(clock)+"をお知らせいたします。")

    # 60秒待つ
    time.sleep(60)
