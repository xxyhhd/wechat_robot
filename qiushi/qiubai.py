import urllib.request
import urllib.parse
from lxml import etree
import settings
from info import Info
from mydb import Mydb


class QiushiSpider():
    # 初始化
    def __init__(self):
        self.db = Mydb()
        self.db.open_file()

    # 释放
    def __del__(self):
        self.db.close_file()

    def run(self):
        url = settings.URL
        headers = settings.HEADERS
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        self.parse(response)  # 解析

    def parse(self, response):
        content = response.read().decode('utf-8')
        html_etree = etree.HTML(content)
        base_path = settings.BASE_XPATH
        base_list = html_etree.xpath(base_path)

        for base in base_list:
            try:
                author = base.xpath(settings.AUTHOR_PATH)[0]
                article = base.xpath(settings.ARTICLE_PATH)[0].xpath('string(.)')
                # print(article)
            except:
                pass
            else:
                # pass
                item = Info(author, article)
                self.db.save_as_json(item)


if __name__ == "__main__":
    spider = QiushiSpider()
    spider.run()