# -*- coding: utf-8 -*-

from requests.exceptions import  ConnectionError, TooManyRedirects, HTTPError
from requests_html import  HTMLSession
from retry import retry

# 試行回数:3 間隔:2 指数:2
# リトライの間隔が2、4、6と増えていく
@retry(tries=3, delay=2, backoff=2)
def get_resp(url):
    try :
        session = HTMLSession()
        return session.get(url)
    except ConnectionError:
        print('Network Error')
        raise
    except TooManyRedirects:
        print('TooManyRedirects')
        raise
    except HTTPError:
        print('BadResponse')
        raise

try:
    r = get_resp('https://search.yahoo.co.jp/realtime')
except:
    print('Response not found')
else:
    li = r.html.find('section.Trend_container__2vkJ-', first=True).text
    print(li)