import requests
import json
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    if r.status_code == 200:
        print
        return r.text
    else:
        print(f"Failed to retrieve the page. Status code: {r.status_code}")
        return None


def parse_html(r):
    if r:
        soup = BeautifulSoup(r, 'html.parser')
        # print(soup.prettify())
        return soup
    else:
        return None

def flipkart(search):
    productlist=[]     
    url="https://www.flipkart.com/search?q="
    page=get_html(url+search)
    soup=parse_html(page)
    titles=soup.find_all('div', class_="_4rR01T")
    prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
    if not len(titles) and not len(prices):
        titles =soup.find_all('a', class_="s1Q9rs")
        prices=soup.find_all('div',class_="_30jeq3")

    for i in range(len(titles)):
        try:
            title = titles[i].text
        except:
            title = "NAN"
        try:
            price = prices[i].text
        except:
            price = "NAN"
        productlist.append(dict({"title":fr"{title}","price":fr"{price}"}))
    strproductlist = str(productlist).replace("'",'"')
    json_data= json.loads(r""+strproductlist)
    return json_data

# a=input("enter your search")     
# data = flipkart(a)
# for item in data:
#     print(item["title"])
#     print(item["price"])
