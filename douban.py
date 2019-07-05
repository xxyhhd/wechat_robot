import urllib.request
import urllib.parse
import json


# data = {
#     'page_limit': 20,
#     'page_start': 40,
# }

# data = urllib.parse.urlencode(data)
# url = url + data
# print(url)


def get_tag():
    url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    respones = urllib.request.urlopen(url=url)
    content = respones.read().decode('utf-8')
    my_json = json.loads(content)
    info = '  '.join(my_json['tags'])
    print('可选电影种类：', info)
    return my_json['tags']


def create_request(a):
    tag = str(input('请输入查询的电影类型：'))
    cate = urllib.parse.quote(tag)
    num = int(input('请输入你需要查询的数量：'))
    page = num//20
    remainder = num % 20
    print('{0:^5}\t{1:{3}^３0}\t{2:^８}'.format('排名', '电影名称', '评分', chr(12288)))
    for x in range(page):
        data = {
            'page_start': x*20,
        }
        data = data = urllib.parse.urlencode(data)
        url = 'https://movie.douban.com/j/search_subjects?type=movie&page_limit=20&sort=rank&' + \
            'tag=' + cate + '&' + data
        respones = urllib.request.urlopen(url=url)
        content = respones.read().decode('utf-8')
        my_json = json.loads(content)
        count = x*20
        for move in my_json['subjects']:
            count += 1
            print('{0:^5}\t{1:{3}^３0}\t{2:^10}'.format(
                count, move['title'], move['rate'], chr(12288)))
    url = 'https://movie.douban.com/j/search_subjects?type=movie&page_limit=20&sort=rank&' + \
        'tag=' + cate + '&' + data
    respones = urllib.request.urlopen(url=url)
    content = respones.read().decode('utf-8')
    my_json = json.loads(content)
    count = page*20
    for move in my_json['subjects'][0:remainder]:
        count += 1
        print('{0:^5}\t{1:{3}^３0}\t{2:^10}'.format(
            count, move['title'], move['rate'], chr(12288)))


def main():
    # get_tag()
    create_request(get_tag())


if __name__ == '__main__':
    main()
