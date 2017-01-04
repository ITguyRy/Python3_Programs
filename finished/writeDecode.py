import requests
from bs4 import BeautifulSoup

def file_name():
    filename = input("What would you like to call your file name? ")
    filetype = input("What file type would you like your file to be? ")
    filename = filename + filetype
    return filename

    
            
def request_url():
    url = 'http://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html)
    return soup
    

def write_filter(soup,filename):
    with open(filename,'w') as file:
        for story_heading in soup.find_all(class_='story-heading'):
            if story_heading.a :
                
               file.write(str(story_heading.a.text.replace('\n'," ").encode('utf-8').strip()))
        
            else:
               file.write(str(story_heading.contents[0].encode('utf-8').strip()))
            


def main():
    filename = file_name()
    soup = request_url()
    write_filter(soup,filename)

main()
