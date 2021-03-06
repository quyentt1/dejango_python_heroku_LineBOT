# -*- encoding: utf-8 -*-
import json
import random
import requests
import sys


from django.shortcuts import render
from django.http import HttpResponse

from bot.load_serif1 import osomatsu_serif

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = '/QcOw5aRu/ca0WkxSFVN9tICSiHkOtFXXWqYFhma1qMTX96c3mnMEutJmFU0OCMM+AICi9tCkoitLttkVbG8eWJz/TOnpLRGKEhKZ7ZFCWxe4D+5mFSeAH7F+/1aWKWkRqACwN6S6xWktfA7GgPjxgdB04t89/1O/w1cDnyilFU='

# Channel Access Token
line_bot_api = LineBotApi('/QcOw5aRu/ca0WkxSFVN9tICSiHkOtFXXWqYFhma1qMTX96c3mnMEutJmFU0OCMM+AICi9tCkoitLttkVbG8eWJz/TOnpLRGKEhKZ7ZFCWxe4D+5mFSeAH7F+/1aWKWkRqACwN6S6xWktfA7GgPjxgdB04t89/1O/w1cDnyilFU=')

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    id1 = "U7e5c77cd35578d742201b0e49a87a058"
  
    return HttpResponse("This is bot api.")


def reply_text(reply_token, text, userid):
    # reply = random.choice(osomatsu_serif)

    # payload = {
    #       "replyToken":reply_token,
    #       "messages":[
    #             {
    #                 "type":"text",
    #                 "text": reply + userid
    #             }
    #         ]
    # }
    message = TextSendMessage(text='Hello, world')
    return line_bot_api.reply_message(reply_token, message)

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8')) # requestの情報をdict形式で取得
    for e in request_json['events']:
        reply_token = e['replyToken']  # 返信先トークンの取得
        message_type = e['message']['type']   # typeの取得
        userid = e['source']['userId'] 
        if message_type == 'text':
            text = e['message']['text']    # 受信メッセージの取得
            reply += reply_text(reply_token, text, userid)   # LINEにセリフを送信する関数

    return HttpResponse(reply)  # テスト用