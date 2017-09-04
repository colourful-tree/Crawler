import requests
from bs4 import BeautifulSoup

url = "http://www.jiuxian.com/goods-"
DOWNLOAD_URL = 'http://www.jiuxian.com/pro/selectProActByProId.htm?'

def download_price(url, id):
        POST_DATA = {'proId':id, 'resId' : 2,}
        try:
            r = requests.post(url,data=POST_DATA,headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            })
        except requests.RequestException as e:
            return -1
        if r.json()["act"]["actPrice"] != -1:
            return "price:"+str(r.json()["act"]["actPrice"])
        elif r.json()["act"]["nowPrice"] != -1:
            return "price:"+str(r.json()["act"]["nowPrice"])
        elif r.json()["act"]["shopPrice"] != -1:
            return "price:"+str(r.json()["act"]["shopPrice"])
        else:
            return -1
        
for i in range(1,500):
    real_url = url + str(i)+".html"
    try:
        r = requests.get(real_url)
    except requests.RequestException as e:
        continue
    html = r.content
    print html

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("div", attrs={"class":"comName"})
    if title == None:
        continue
    print "----------"
    print real_url
    print title.get_text().encode("utf-8").strip()
    
    print download_price(DOWNLOAD_URL,str(i))
    
    content_list = soup.find("ul", attrs={"class":"intrList clearfix"})
    if content_list != None:
        p_list = content_list.find_all("li")
        for i in p_list:
            print i.get_text().encode("utf-8").replace(" ","")

