import requests
from bs4 import BeautifulSoup




def request_url():
    url = 'http://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html)
    return soup
    

def filtering(soup):
        
    for story_heading in soup.find_all(class_='story-heading'):
        if story_heading.a :
            
            print(story_heading.a.text.replace('\n',"").strip())
            
        else:
           print(story_heading.contents[0].strip())

def main():
    soup = request_url()
    filtering(soup)

main()
