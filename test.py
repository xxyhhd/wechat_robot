import itchat
import requests
from get_univ import main

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'  # 图灵机器人的api
    data = {
        'key': 'df34a6f4062c41e39e8239d4c98e809a',  # Tuling Key
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    print(r.get('text'))
    return r.get('text')


# 用于接收来自朋友间的对话消息，如果不用这个，朋友发的消息便不会自动回复
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def print_content(msg):
    try:
        if itchat.search_friends(userName=msg['FromUserName'])['NickName'] in ['Rain']\
                or itchat.search_chatrooms(userName=msg['FromUserName'])['NickName'] in ['测试']:
            if msg['Text'] == '大学排名':
                return main()
            else:
                print(msg['Text'])
                return get_response(msg['Text'])
    except:
        print(msg)
        print('其他人消息')


# 用于接收来自朋友间的对话消息，如果不用这个，朋友发的消息便不会自动回复
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def print_content(msg):
    try:
        if itchat.search_chatrooms(userName=msg['FromUserName'])['NickName'] in ['测试']:
            if msg['Text'] == '大学排名':
                return main()
            else:
                print(msg['Text'])
                return get_response(msg['Text'])
    except:
        print(msg)
        print('其他群消息')


itchat.auto_login(True)
itchat.run()
