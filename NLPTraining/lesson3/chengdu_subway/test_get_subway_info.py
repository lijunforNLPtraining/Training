

import re
import requests
from collections import defaultdict



headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
url_subway = 'https://baike.baidu.com/item/%E6%88%90%E9%83%BD%E5%9C%B0%E9%93%81'

content = requests.get(url_subway, headers=headers).content.decode('utf8').replace('\n', '')

## Get stations' name and url ##
str_beg = '<h3 class="title-text"><span class="title-prefix">成都地铁</span>运营线路</h3>'
str_end = '备注：以上信息据2018年12月26日成都地铁官网显示。<sup class="sup--normal" data-sup="1">'
pattern = re.compile(str_beg + '(.*)' + str_end)

need_content = re.findall(pattern, content)[0]
# print(need_content)

subway_pat = re.compile('<td width="90" align="center" valign="middle">'
                        '<a target=_blank href="(.+?)">(.+?)</td>')
subway_paths = re.findall(subway_pat, need_content)
# print(subway_pat)
# print(subway_paths)
path_list = []

for (url, name) in subway_paths:
    # print(url)
    # print(name)
    url = 'https://baike.baidu.com' + url
    name = name.replace('</a>', '')
    path_list.append((url, name))

for (url, name) in path_list:
    print('url: ', url)
    print('name: ', name)

path_num = len(path_list)#一共有多少条地铁线路














