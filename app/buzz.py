import requests
from bs4 import BeautifulSoup

class buzz():

    def __init__(self, input_):
        self.titles= list()
        self.prices = list()
        self.size = 0

        input_ = input_.split(' ')
        # print(input_)
        for n in range(len(input_)):
            temp = list()
            if input_[n] != "":
                temp.append(input_[n])
        input_ = temp


        last = input_[len(input_)-1]
        input_.remove(last)
        final = str()

        for words in input_:
            final += str(words) + "+"
        final += last

        # print(final)

        url =  "https://www.buzzsneakers.com/MAK_mk/proizvodi?search={}".format(final)
        # print(url)

        html = requests.get(url=url)

        soup = BeautifulSoup(html.text, 'html.parser')

        posts = soup.find_all(class_='hidden-fullscreen')

        next1 = posts[1].find(class_='container hidden-fullscreen')

        next2 = next1.find(class_='row listing-products')

        next3 = next2.find(class_='col-xs-12 col-sm-9 col-lg-10')

        next4 = next3.find_all(class_='row')

        
        for finds in next4:
            titiles = finds.find_all(class_='title')
            for title in titiles:
                self.titles.append(title.get_text()
                .replace('\n','')
                .lstrip()
                .rstrip())
                self.size += 1

        for finds in next4:
            prices = finds.find_all(class_='current-price')
            for price in prices:
                self.prices.append(price.get_text()
                .replace('\n','')
                .replace('MKD','')
                .lstrip()
                .rstrip())
        

