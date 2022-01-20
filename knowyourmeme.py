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
        search_url = "http://knowyourmeme.com/memes/" + term  # making a url to be used
        page = requests.get(search_url, headers=_HEADERS)  # requesting code
        soup = BeautifulSoup(page.content, 'html.parser')  # parsing code with Beautiful Soup
        return self.parse(page.content)


    def random_image(self):
        url = "http://knowyourmeme.com/photos/random"
        page = requests.get(url, headers=_HEADERS)  # requesting code
        return self.parse(page.content)


    def parse(self, content):
        try:
            soup = BeautifulSoup(content, 'html.parser')  # parsing it
            title = soup.find('meta', attrs={"property": "og:title"})['content']  # finding description
            description = soup.find('meta', attrs={"name": "description"})['content']  # finding description
            #siteurl = soup.find('meta', attrs={"property": "og:url"})['content']  # finding site url
            image = soup.find('meta', attrs={"property": "og:image"})['content']  # finding image url

            result = f"{title} \n {description} \n {image}"
            print(result)
            return result
        except:
            result = "No results found for your meme :sob:"
            print(result)
            return result

#if __name__ == '__main__':
#    kym = KnowYourMeme() 
#    kym.search('pepehands')
#    #kym.random_image()


