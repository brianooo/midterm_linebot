##########
#製作小遊戲
##########

from linebot.models import (
    ImagemapSendMessage,TextSendMessage,ImageSendMessage,LocationSendMessage,FlexSendMessage,VideoSendMessage,StickerSendMessage,AudioSendMessage
)
import random
import json

def dictionary():
    answers = {}
    answers['red'] = '赤蠵龜'
    answers['green'] = '綠蠵龜'
    answers['olive'] = '欖蠵龜'
    answers['hawk'] = '玳瑁'
    answers['leather'] = '革龜'
    return answers

# 加入好友的小遊戲
def welcome_game():
    kinds = ['red', 'green', 'olive', 'hawk', 'leather']
    pic = kinds[random.randint(0, 4)] + '_' + str(random.randint(1, 5)) + '.jpg'
    question = 


