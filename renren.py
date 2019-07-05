import urllib.request
import urllib.parse
import http.cookiejar
import json


cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)


post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019651354277'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
form_data = {
    'email': '15620569943',
    'icode': '', 
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '859a12c8d87dd25ee379ae206146390020d298612535bbb59cf29bacd5e2402e',
    'rkey': 'd0cf42c2d3d337f9e5d14083f2d52cb2',
    'f':'', 
}
# post做数据编码
data = urllib.parse.urlencode(form_data).encode('utf-8')
req = urllib.request.Request(data=data, url=post_url, headers=headers)
response = opener.open(req)

print(response.getcode())

my_url = 'http://www.renren.com/551403626/profile'
my_req = urllib.request.Request(url=my_url)
my_response = opener.open(my_req)
print(my_response.read().decode('utf-8'))