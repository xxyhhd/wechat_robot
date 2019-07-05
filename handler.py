import urllib.request
import urllib.parse

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

req = urllib.request.Request(url=url, headers=headers)

# 构造更高级的请求对象
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(req)

print(response.read().decode('utf-8'))