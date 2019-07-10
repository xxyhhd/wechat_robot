import urllib.request
import urllib.parse
from lxml import etree
# import settings
# from info import Info
# from mydb import Mydb


class QiushiSpider():
    # 初始化
    def __init__(self):
        self.HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        self.URL = 'https://www.qiushibaike.com/hot/'

        self.BASE_XPATH = '//*[@class="article block untagged mb15 typs_hot"]'
        self.AUTHOR_PATH = './div[1]/a[2]/h2/text()'
        self.ARTICLE_PATH = './a[@class="contentHerf"]/div/span'
        # pass
        # self.db = Mydb()
        # self.db.open_file()

    # 释放
    def __del__(self):
        pass
        # self.db.close_file()

    def run(self):
        url = self.URL
        headers = self.HEADERS
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        # print(1)
        return self.parse(response)  # 解析

    def parse(self, response):
        content = response.read().decode('utf-8')
        html_etree = etree.HTML(content)
        base_path = self.BASE_XPATH
        base_list = html_etree.xpath(base_path)

        # for base in base_list:
        try:
            import random
            base = base_list[random.randint(0, len(base_list))]
            author = base.xpath(self.AUTHOR_PATH)[0]
            article = base.xpath(self.ARTICLE_PATH)[
                0].xpath('string(.)')
            # print('本文来自糗事百科\n作者:{}{}'.format(author, article))
            # return '1'
            return '本文来自糗事百科\n作者:{}{}'.format(author, article)
        except:
            print(2)
            return '出问题了'
        # else:
        #     pass
            # item = Info(author, article)
            # self.db.save_as_json(item)


if __name__ == "__main__":
    pass
# spider = QiushiSpider()
# print(spider.run())