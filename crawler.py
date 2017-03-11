import requests
from bs4 import BeautifulSoup

url = "http://www.jiuxian.com/goods-31071.html"

for i in range(0,1):
    r = requests.get(url)
    
    html = r.content
    print html

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("div", attrs={"class":"comName"})
    print title.get_text().encode("utf-8").strip()

    content_list = soup.find("ul", attrs={"class":"intrList clearfix"})
    if content_list != None:
        p_list = content_list.find_all("li")
        for i in p_list:
            print i.get_text().encode("utf-8").replace(" ","")
