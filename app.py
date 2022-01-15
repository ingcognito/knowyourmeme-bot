import requests
from bs4 import BeautifulSoup

_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}  # defining headers for browser


class KnowYourMeme:
    def __init__(self):
        self.about = None
        self.imageurl = None
        self.siteurl = None
        self.soup = None


    def search(self, term):
        for i in term:  # change every space to +
            if i == " ":
                i = "+"
        search_url = "http://knowyourmeme.com/search?q=" + term  # making a url to be used
        page = requests.get(search_url, headers=_HEADERS)  # requesting code
        soup = BeautifulSoup(page.content, 'html.parser')  # parsing code with Beautiful Soup

        list1 = soup.findAll("a", href=True)  # Finding all links of search
        url2 = "http://knowyourmeme.com" + list1[129]['href']  # Picking first result and using its href
        page2 = requests.get(url2, headers=_HEADERS)  # requesting page again
        self.parse(page2.content)



    def random_image(self):
        url = "http://knowyourmeme.com/photos/random"
        page = requests.get(url, headers=_HEADERS)  # requesting code
        self.parse(page.content)


    def parse(self, content):
        soup = BeautifulSoup(content, 'html.parser')  # parsing it
        about = soup.find('meta', attrs={"property": "og:title"})['content']  # finding description
        imageurl = soup.find('meta', attrs={"property": "og:image"})['content']  # finding image url
        # siteurl = soup.find('meta', attrs={"property": "og:url"})['content']  # finding site url
        print(f"{about} - {imageurl}")
        #print(about['content'])
        #return about['content']  # This is used for you to be able to print object and get definition print(nameofobject)

if __name__ == '__main__':
    kym = KnowYourMeme() 
    kym.search('asdf')
    kym.random_image()
