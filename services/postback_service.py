'''
用戶點選圖文選單選項時，可以統計使用紀錄
然後不同的選項做出不同的處理方式

'''

from models.user import User
from services.user_service import UserService
from daos.user_dao import UserDAO
from flask import Request
from linebot import (
    LineBotApi
)

import os
from daos.user_dao import UserDAO
from controllers.line_bot_controller import key_image

#引入所需要的消息與模板消息
from linebot.models import(
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
    TemplateSendMessage , PostbackEvent, ImageMessage,
    MessageAction, URIAction, PostbackAction, DatetimePickerAction, CameraAction, CameraRollAction, LocationAction,
    QuickReply, QuickReplyButton
)

#引入按鍵模板，另外還有確認範本(ConfirmTemplate)、圖片輪播範本(CarouselTemplate)
from linebot.models.template import(
    ButtonsTemplate, CarouselTemplate
)

from utils.reply_send_message import detect_json_array_to_new_message_array

class PostbackService:
    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    def __init__(cls, event):
        cls.user_id = cls.line_bot_api.get_profile(event.source.user_id)
        cls.user = UserService.get_user(cls.user_id)
        cls.event = event

    # Data1 => 龜去來戲，丟題目 QuickReply
    @classmethod
    def postback_data1(cls):
        cls.user.line_user_click["Data1"] += 1
        # 存入資料庫
        UserDAO.save_user(cls.user)

        cls.line_bot_api.reply_message(
            cls.event.reply_token,
            TextSendMessage(text="龜去來戲功能尚未上線，敬請期待。")
        )

    # Data2 => 世界龜寶，丟出參考資料
    @classmethod
    def postback_data2(cls):
        cls.user.line_user_click["Data2"] += 1
        # 存入資料庫
        UserDAO.save_user(cls.user)

        # 丟出輪播範本
        result_message_array = detect_json_array_to_new_message_array("data2_message_json/carousel1_message.json")
        cls.line_bot_api.reply_message(
            cls.event.reply_token,
            result_message_array
        )

    # Data3 => 幫你龜類，啟動相機或上傳圖片
    @classmethod
    def postback_data3(cls):
        cls.user.line_user_click["Data3"] += 1
        # 存入資料庫
        UserDAO.save_user(cls.user)

        # 丟出按鍵範本
        result_message_array = detect_json_array_to_new_message_array("data3_message_json/button_template_message.json")
        cls.line_bot_api.reply_message(
            cls.event.reply_token,
            result_message_array
        )
        key_image = True

    # Data4 => 我的龜密，丟出參考資料
    @classmethod
    def postback_data4(cls):
        cls.user.line_user_click["Data4"] += 1
        # 存入資料庫
        UserDAO.save_user(cls.user)

        # 回傳相關訊息
        result_message_array = detect_json_array_to_new_message_array("data4_message_json/default_text_message.json")
        cls.line_bot_api.reply_message(
            cls.event.reply_token,
            result_message_array
        )


    # Data5 => 殊途同龜，丟出參考資料
    @classmethod
    def postback_data5(cls):
        cls.user.line_user_click["Data5"] += 1
        # 存入資料庫
        UserDAO.save_user(cls.user)

        # 回傳相關訊息
        result_message_array = detect_json_array_to_new_message_array("data5_message_json/data5_text_message.json")
        cls.line_bot_api.reply_message(
            cls.event.reply_token,
            result_message_array
        )

    # Data6 => 默守成龜，丟出參考資料
    @classmethod
    def postback_data6(cls):
        cls.user.line_user_click["Data6"] += 1
        # 存入資料庫
        UserDAO.save_user(cls.user)

        # 回傳相關訊息
        result_message_array = detect_json_array_to_new_message_array("data6_message_json/data6_text_message.json")
        cls.line_bot_api.reply_message(
            cls.event.reply_token,
            result_message_array
        )