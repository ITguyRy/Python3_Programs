from bs4 import BeautifulSoup
import requests

def request_url():
    url = ' http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text

    theGoods = BeautifulSoup(r_html)
    return theGoods

def sort(theGoods):

    for articles in theGoods.find_all(class_="component-article"):
        print(articles)

def main():
    theGoods = request_url()
    sort(theGoods)

main()

