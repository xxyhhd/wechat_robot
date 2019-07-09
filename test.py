from urllib import request, parse
from lxml import etree
import http.cookiejar


# 检查翻译源是否有汉语
def check_chinese(query):
    for ch in query.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


# 构造url
def create_url(query):
    if check_chinese:
        url = 'https://fanyi.baidu.com/?aldtype=16047#en/zh/'
    else:
        url = 'https://fanyi.baidu.com/?aldtype=16047#zh/en/'
    query = request.quote(query)
    # print(url + query)
    return url + query


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    cookie = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    query = str(input('请输入需要翻译的语句：'))
    url = create_url(query)

    req = request.Request(url=url, headers=headers)
    response = opener.open(req)
    html_content = response.read().decode('utf-8')

    file_name = 'tieba' + '.html'
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(html_content)

    # my_xpath = '//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[1]/text()'
    # my_xpath = '//p[@class="ordinary-output source-output xh-highlight"]/text()'
    # html_tree = etree.HTML(html_content)
    # print(html_tree)
    # data_list = html_tree.xpath(my_xpath)
    # print(data_list)
    # for i in data_list:
    #     print(i)


if __name__ == "__main__":
    main()
# <p class="ordinary-output source-output xh-highlight" dir="ltr" style="display:none;">你是谁</p>
