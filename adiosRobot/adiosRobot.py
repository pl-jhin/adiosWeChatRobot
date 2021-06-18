#coding='utf-8'
import requests
import random
import urllib.request
from bs4 import BeautifulSoup
def rjcsdrz():
    with open(r"D:\projectPython\PyWeChatSpy-master\adiosRobot\我在人间凑数的日子.txt","r",encoding='utf-8') as f:
        data = f.readlines()
        str = random.choice(data).strip('\n')
        return str

def chengyujielong(search):
    list=[]
    print(search)
    baseUrl = "http://www.chengyujielong.com.cn/search/"+urllib.parse.quote(search)
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }
    request = urllib.request.Request(baseUrl, headers=head)
    html = ""
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    itemSoup = soup.find("div", class_="panel-body")
    for item in itemSoup.findAll("li"):
        list.append(item.text)
    print(list)
    return list

def testList():
    wxGroup = ["123123", "456456456", "678678678", "000"]
    for group in wxGroup:
        print(group)
    print("================")
    if "00" not in wxGroup:
        wxGroup.append("00")
    for group in wxGroup:
        print(group)
def getChenYu(str):
    return str[-2]
if __name__ == '__main__':
    print(getChenYu("👉身不由己👈"))