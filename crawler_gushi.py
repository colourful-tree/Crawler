import requests
from bs4 import BeautifulSoup

url = "http://www.tonghua5.com"

url_total = url + "/jingdiantonghua/"
try:
    r = requests.get(url_total)
except requests.RequestException as e:
    print "error"
html = r.content
soup = BeautifulSoup(html, "html.parser")
all_index = soup.find("div", attrs={"class":"pagepage"})
index_pages = []
if all_index != None:
    p_list = all_index.find_all("a")
    for i in p_list:
        index_pages.append(url + i["href"])

all_url = []
for i in index_pages:
    try:
        r = requests.get(i)
    except requests.RequestException as e:
        continue
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    urls = soup.find("ul", attrs={"class":"d2 ico3"})
    if urls != None:
        p_list = urls.find_all("li")
        for page in p_list:
            tmp = page.find("a")
            if tmp != None:
                all_url.append(url + tmp["href"])

for url_i in all_url:
#for i in range(284, 413):
#for i in range(284, 290):
    #real_url = url + "/gelin/" + str(i)+".html"
    try:
        #r = requests.get(real_url)
        r = requests.get(url_i)
    except requests.RequestException as e:
        continue
    html = r.content
    #print html

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("div", attrs={"class":"title"})
    if title == None:
        continue
    #print "----------"
    #print real_url
    title = title.get_text().encode("utf-8").strip()
    content = []
    content_list = soup.find("div", attrs={"class":"content 2"})
    if content_list != None:
        p_list = content_list.find_all("p")
        for i in p_list:
            content.append(i.get_text().encode("utf-8").replace(" ",""))

    next_pages = []
    next_page_list = soup.find("div", attrs={"class":"pagepage"})
    if next_page_list != None:
        p_list = next_page_list.find_all("a")
        for i in p_list:
            next_pages.append( url + i["href"])
        next_pages = next_pages[1:]
        #print next_pages
        for i in next_pages:
            try:
                r = requests.get(i)
            except requests.RequestException as e:
                continue
            html = r.content
            #print html
            soup = BeautifulSoup(html, "html.parser")
            content_list = soup.find("div", attrs={"class":"content 2"})
            if content_list != None:
                p_list = content_list.find_all("p")
                for i in p_list:
                    content.append(i.get_text().encode("utf-8").replace(" ",""))
    #print real_url + "\t" + title + "\t" + " ".join(content)

    res = url_i.encode("utf-8") + "\t" + title + "\t" + " ".join(content)
    print res
