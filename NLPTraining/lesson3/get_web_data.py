

import requests
import re
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    except:
        return 'craw failed'



if __name__ == '__main__':
    url = 'https://baike.baidu.com/item/北京地铁/408485'
    soup = getHtmlText(url)
    print(soup)
























