from __future__ import unicode_literals
from PIL import ImageGrab
import os
import time
from threading import Timer
from wxpy import *
from get_univ import main



  # 登录微信
path = r'D:\a_picture'


# def get_picture():
#     picture = ImageGrab.grab((800, 200, 1200, 600))
#     picture_name = time.strftime('%H-%M-%S', time.localtime())
#     picture.save(os.path.join(path, picture_name+'.jpg'))
#     return picture_name


def send_news():
    bot = Bot()
    try:
        my_friend = bot.friends().search('许祥雨')[0]
        # print(my_friend)
        # name = get_picture()
        # news = os.path.join(path, name+'.jpg')
        # print(news)
        news = main()
        my_friend.send_image(news)
        my_friend.send('发送成功')
        # bot.join()
        print('发送成功')
        t = Timer(60, send_news)  # 设置发送间隔
        t.start()
    except:
        print('发送失败')

def nes():
    a = main()
    print(type(a))
    print(a)

if __name__ == '__main__':
    send_news()
