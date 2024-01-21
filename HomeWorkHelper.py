import bs4 as bs
import urllib.request
import time

class HomeWorkHelper:
    def __init__(self):
        self.brainly_links = []

    def HomeWorkHelper(self, question, repeats):
        self.question = "brainly " + str(question)
        self.url = "https://www.bing.com/search?q=" + repr(self.question.replace(" ","+"))
        self.repeats = repeats

        for i in range(self.repeats):
            source = urllib.request.urlopen(self.url).read()
            soup = bs.BeautifulSoup(source,'html.parser')
            links = soup.find_all('a')

            for link in links:
                href = link.get('href')
                if href and 'brainly.com/question/' in href:
                    
                    if href in self.brainly_links:
                        continue
                    self.brainly_links.append(href)
        links = self.brainly_links
        self.brainly_links = []
        return links


