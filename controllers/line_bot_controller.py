'''
當用戶關注時，必須取用照片，並存放至指定bucket位置，而後生成User物件，存回db
當用戶取消關注時，
    從資料庫提取用戶數據，修改用戶的封鎖狀態後，存回資料庫
'''

from linebot import (
    LineBotApi, WebhookHandler
)
import os

# 載入Follow事件
from linebot.models.events import (
    FollowEvent, UnfollowEvent
)

from services.image_service import ImageService
from services.user_service import UserService
from services.video_service import VideoService
from services.audio_service import AudioService
from services.postback_service import PostbackService
from services.text_service import TextService

from urllib.parse import parse_qs

global key_image

class LineBotController:

    # 將消息交給用戶服務處理
    @classmethod
    def follow_event(cls, event, richmenuid):
        # print(event)
        UserService.line_user_follow(event, richmenuid)

    @classmethod
    def unfollow_event(cls, event):
        UserService.line_user_unfollow(event)

    # 未來可能會判斷用戶快取狀態
    # 現在暫時無
    @classmethod
    def handle_text_message(cls, event):
        TextService.line_user_textSend(event)
        return "OK"

    # 用戶收到照片時的處理辦法
    @classmethod
    def handle_image_message(cls, event):
        ImageService.line_user_upload_image(event, key=key_image)
        return "OK"

    # 用戶收到影片時的處理辦法
    @classmethod
    def handle_video_message(cls, event):
        VideoService.line_user_upload_video(event)
        return "OK"

    @classmethod
    def handle_audio_message(cls, event):
        AudioService.line_user_upload_video(event)
        return "OK"

    # 擷取event的data欄位，並依照function_name，丟入不同的方法
    @classmethod
    def handle_postback_event(cls, event):

        # query string 拆解 event.postback.data
        # query_string_dict = parse_qs(event.postback.data)

        # 擷取功能
        # detect_function_name = query_string_dict.get('function_name')[0]

        # Postbakc function 功能對應轉發
        post = PostbackService(event)

        if event.postback.data == 'Data1':
            post.postback_data1()
        elif event.postback.data == 'Data2':
            post.postback_data2()
        elif event.postback.data == 'Data3':
            post.postback_data3()
        elif event.postback.data == 'Data4':
            post.postback_data4()
        elif event.postback.data == 'Data5':
            post.postback_data5()
        elif event.postback.data == 'Data6':
            post.postback_data6()
        else:
            pass


        return 'OK'