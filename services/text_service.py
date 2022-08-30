from multiprocessing import resource_sharer
from models.user import User
from flask import Request
from linebot import (
    LineBotApi
)

import os
from daos.user_dao import UserDAO
from linebot.models import (
    TextSendMessage, TemplatSendMessage
)

from linebot.models.template import(
    ButtonsTemplate, CarouselTemplate
)

kinds_template = TemplatSendMessage(
    alt_text = 'Carousel Template',
    template = CarouselTemplate(
        "type": "image_carousel",
        "columns": [
            {
                "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5HsB39IEVz6K6R27Sy8msBk2NMRskhvm35ZjqlUMVkN__lfWwiD_bvs9LNuMat38_F1A&usqp=CAU",
                "action": {
                    "type": "uri",
                    "label": "有哪些種類? 維基去",
                    "uri": "https://zh.wikipedia.org/zh-tw/海龟"
                    }
            }
        ]
    )
)

conservation_template = TemplatSendMessage(
    alt_text = 'Carousel Template',
    template = CarouselTemplate(
        "type": "image_carousel",
        "columns": [
            {
                "imageUrl": "https://resource01-proxy.ulifestyle.com.hk/res/v3/image/content/2760000/2760970/18EJ014__20200924_L.jpg",
                "action": {
                "type": "uri",
                "label": "海龜保育計畫",
                "uri": "https://www.oca.gov.tw/userfiles/A47020000A/files/海龜保育計畫(草案).pdf"
                }
            },
            {
                "imageUrl": "https://imgcdn.cna.com.tw/www/WebPhotos/800/20220523/1365x768_20220523000005.jpg",
                "action": {
                "type": "uri",
                "label": "海洋公民科學家推廣",
                "uri": "https://www.oca.gov.tw/filedownload?file=sustainable/202012311108491.pdf&filedisplay=109年度海洋公民科學家推廣培訓計畫-海龜.pdf&flag=trans"
                }
            }
        ]
    )
)

friendly_template = TemplatSendMessage(
    alt_text = 'Carousel Template',
    template = CarouselTemplate(
        "type": "image_carousel",
        "columns": [
            {
                "imageUrl": "https://avier.com.tw/files/ck/images/STT.JPG"
                "action": {
                "type": "uri",
                "label": "對待好龜密",
                "uri": "https://event.oac.gov.tw/kids/home.jsp?id=63&parentpath=0,6"
                }
            }
        ]
    )
)

rescue_template = TemplatSendMessage(
    alt_text = 'Carousel Template',
    template = CarouselTemplate(
        "type": "image_carousel",
        "columns": [
            {
                "imageUrl": "https://uc.udn.com.tw/photo/2021/10/12/realtime/14268224.jpg"
                "action": {
                "type": "uri",
                "label": "救援組織網",
                "uri": "https://www.oca.gov.tw/ch/home.jsp?id=376&parentpath=0,296,375"
                }
            }
        ]
    )
)

template_message_dict = {
    "@海龜種類": kinds_template,
    "@海龜生存及保育": conservation_template,
    "@友善海龜指南": friendly_template,
    "@海保救援": rescue_template,
}


class TextService:
    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    @classmethod
    def line_user_textSend(cls, event):
        if (event.message.text.find('@') != -1):     # 有特殊記號
            cls.line_bot_api.reply_message(
                event.reply_token,
                template_message_dict.get(event.message.text)
            )
        else:
            cls.line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="我是你的龜密，請點選選單喔 !!")
            )


