# -*- coding:UTF-8 -*-
import requests
#import requests.packages
#import requests.packages.urllib3.util.ssl_
from bs4 import BeautifulSoup

#requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

def download_info(url):
    try:
        r = requests.get(url, headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/534.20' })
    except requests.RequestException as e:
        print e
    html = r.content
    print html
    if html.find("北京") != -1 and html.find("关注她") != -1:
        return True
    else:
        return False

def main():
    url = "https://www.zhihu.com/question/30400300"
    page = 10
    for i in range(1, page):
        real_url = url + "/?page=" + str(i)
        print real_url
        try:
            r = requests.get(real_url, headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/534.20' })
            html = r.content
            print html
            soup = BeautifulSoup(html, "html.parser")
            content_list = soup.find_all("div", attrs={"class":"AuthorInfo"})
            for i in content_list:
                p = i.find("meta", attrs={"itemprop":"url"})
                people_url = p["content"]
                if download_info(people_url):
                    print people_url
        except requests.RequestException as e:
            print e

        

main()
