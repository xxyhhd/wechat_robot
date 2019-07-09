'''
负责基本信息的配置
１．　xpath路径的配置
２．　header配置
３．　代理的配置
４．　验证码识别的配置
５．　全局变量的配置
'''


HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
URL = 'https://www.qiushibaike.com/hot/'

BASE_XPATH = '//*[@class="article block untagged mb15 typs_hot"]'
AUTHOR_PATH = './div[1]/a[2]/h2/text()'
ARTICLE_PATH = './a[@class="contentHerf"]/div/span'

