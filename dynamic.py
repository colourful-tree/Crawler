import requests
import json
import codecs

DOWNLOAD_URL = 'http://www.jiuxian.com/pro/selectProActByProId.htm?t=1488941230548'
def download_page(url):
        POST_DATA = {'proId':'600','resId' : 2,}
        r = requests.post(url,data=POST_DATA,headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
         })

        return r.json()
        
j = download_page(DOWNLOAD_URL)
#print j
print j["act"]["actPrice"]
