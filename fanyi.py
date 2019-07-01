import requests
import json

url = 'https://fanyi.baidu.com/v2transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'cookie': 'BAIDUID=0CCBCF9B59BCAE173397128C9689B9D2:FG=1; BIDUPSID=0CCBCF9B59BCAE173397128C9689B9D2; PSTM=1528346886; BDUSS=WdyMThyc1hOUGxYWlFlb3RabTdiLVlMTDhKSmVjZlBmbjNsU2lIUm1ETkQtRlZiQVFBQUFBJCQAAAAAAAAAAAEAAADX4bw3z-DLvNPqNzc3Nzc3NzcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAENrLltDay5bR; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=2; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; ZD_ENTRY=baidu; session_id=1561987004264; session_name=www.baidu.com; H_PS_PSSID=26522_1432_21093_29073_29237_28519_29099_28839_29221_29439_22157; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1561778405,1561783207,1561982534,1561987660; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1561987660; yjs_js_security_passport=ff5d270bbf6e10e291c84182459d33f8be440d15_1561987668_js',
}


def check_chinese(query):
    for ch in query.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def baidu(query):
    data1 = {
        'from': 'en',
        'to': 'zh',
        'query': query,
        # 'transtype': 'translang', 可以注释的字段
        # 'simple_means_flag': '3', 可以注释的字段
        'sign': '456029.136812',
        'token': '683809aabb0830223d1fee0bd38cd700'
    }

    data2 = {
        'from': 'zh',
        'to': 'en',
        'query': query,
        'transtype': 'translang',
        'simple_means_flag': '3', 
        'sign': '637195.875066',
        'token': '683809aabb0830223d1fee0bd38cd700'
    }
    if check_chinese:
        data = data2
    else:
        data = data1
    res = requests.post(url, data=data, headers=headers)
    str_json = res.content.decode('utf-8')
    myjson = json.loads(res.content)
    return myjson['trans_result']['data'][0]['dst']

