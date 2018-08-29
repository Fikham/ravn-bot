import os, sys
from argparse import ArgumentParser
from urllib.parse import quote
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler)
from linebot.exceptions import (
    InvalidSignatureError)
from linebot.models import (
    MessageEvent, TextMessage, ImageSendMessage, TextSendMessage)

# import eksekutor.py, yang di dalamnya memuat modul-modul keyword
from eksekutor import *

app = Flask(__name__)

channel_secret      = os.getenv('34beb3c1864393ec04b41fb89e9e748b', None)
channel_access_token= os.getenv('3FleT/GGZbr22Wy0UoF5wKRIpX1OFYnpvfmIi9jveZGuxIwIN3/FMZxX6aOJaoniB819fV6Xw4rHRoK34om/aOxaGeCpbcDkty37MD2eaV9MuDr7/MGvWCa3wZF2HMODDX073wLApgUjwEiLw4L01gdB04t89/1O/w1cDnyilFU=', None)
line_bot_api        = LineBotApi(channel_access_token)
handler             = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# pengolahan keyword-keyword
@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    tipe, data  = Process(event.message.text)
    if tipe=='Text':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=data))
    elif tipe=='Image':
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=data,
                preview_image_url=data)
            )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
