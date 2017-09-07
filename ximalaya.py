import requests
from bs4 import BeautifulSoup
import json
import urllib

def getHtml(url):
    r = requests.get(url,headers={
                                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
                })
    return r.content
aaa = []
with open("url" ,"r") as fin:
    for i in fin:
        aaa.append(i.strip())

for aa in aaa:
    url = "http://www.ximalaya.com/18522984/album/" + aa + "/"
    print url
    html = getHtml(url)
#print html

    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("div", attrs={"class":"detailContent_title"})
    if title != None:
        title = title.get_text().encode("utf-8").strip()

    sub = soup.find("div", attrs={"class":"mid_intro"})
    if sub != None:
        sub = sub.get_text().encode("utf-8").strip()

    all_pages = []
    next_page_list = soup.find("div", attrs={"class":"pagingBar_wrapper"})
#print next_page_list
    if next_page_list != None:
        p_list = next_page_list.find_all("a")
        #print len(p_list)
        for i in p_list:
            all_pages.append(("http://www.ximalaya.com" + i["href"]).encode("utf-8"))
        all_pages = all_pages[1:-1]
    all_pages = [url] + all_pages

    pv = []
    for each_page in all_pages:
        html_i = getHtml(each_page)
        soup_i = BeautifulSoup(html_i, "html.parser")
        album_soundlist = soup_i.find("div", attrs={"class":"album_soundlist is_more"})
        if album_soundlist == None:
            album_soundlist = soup_i.find("div", attrs={"class":"album_soundlist"})

        if album_soundlist != None:
            p_list = album_soundlist.find_all("li")
            for i in p_list:
                k = i.find("a", attrs={"class":"title"}).get_text().strip().encode("utf-8")
                v = i.find("span", attrs={"class":"sound_playcount"}).get_text().strip().encode("utf-8")
                pv.append({k:v})
    res = {}
    res["title"] = title
    res["abstract"] = sub
    res["pv"] = pv
    result = json.dumps(res, ensure_ascii=False)
#print result
    with open("res.txt", "a") as fout:
        fout.write("\n" + result)
