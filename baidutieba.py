import urllib.request
import urllib.parse
import json



# 构造请求
def create_request(keyword, page):
    base_url = 'http://tieba.baidu.com/f?'
    data = {
        'kw': keyword,
        'pn': (page-1)*50
    }
    data = urllib.parse.urlencode(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Cookie': 'BAIDUID=7E10C8890AE422B60DD798989F2298C8:FG=1; BIDUPSID=7E10C8890AE422B60DD798989F2298C8; PSTM=1561951326; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; yjs_js_security_passport=0bc1d118ce95b89dc0c0610d11f3078697a9f0a9_1562232138_js; TIEBAUID=cb23caae14130a0d384a57f1; TIEBA_USERTYPE=a043d10a15799174661a82c3; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1562300432; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1562301215',
    }
    url = base_url + data
    return urllib.request.Request(url=url, headers=headers)  # 构造请求


# 请求数据
def request_data(req):
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    return content


# 保存函数
def save_data(content, path, page):
    file_name = path + 'tieba' + str(page) + '.html'
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(content)


# 主函数
def main():
    # keyword = str(input('请输入你要搜索的内容'))
    # page = int(input('请输入你要搜索的页数'))
    keyword = 'python'
    page = 3
    path = ''
    req = create_request(keyword, page)
    content = request_data(req)
    # save_data(content,path, page)
    print(content)


if __name__ == '__main__':
    main()
