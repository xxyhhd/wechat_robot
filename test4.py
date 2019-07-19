'''
登录时需要验证码，每次访问验证码链接都会更换，需要使用session去下载验证码图片
登录表单有隐藏项，且每次都随机刷新，需要先用session去获取当前的隐藏值
'''

import requests
from bs4 import BeautifulSoup


s = requests.session()  # 定制session

url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

r = s.get(url=url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')
value_1 = soup.select('#__VIE')[0].attrs.get('value') # form表单里的必须选项，服务器随机生成

img_url = 'http://so.gushiwen.org' + soup.select('#id2')[0].attrs.get('src')　# 获取验证码的链接

img = s.get(img_url)　

with open('./randcode.jpg', 'wb') as fp: # 二进制写
    fp.write(img.content) # 二进制写入

code = '通过第三方验证平台获取验证码'

data = {
    'value_1': value_1,
    'username': 'xxy',
    'password': 'www',
    'code': code
}

r = s.post(url=url, data=data, headers=headers)
with open('login.html', 'w', encoding='utf-8') as fp:
    fp.write(r.text)