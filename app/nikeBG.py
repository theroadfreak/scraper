import requests
from bs4 import BeautifulSoup
from utils import myString



class nikeBG():

    def __init__(self, input_):
        self.name = "NIKE BG"
        self.titles= list()
        self.prices = list()
        self.size = 0

        url = "https://www.nike.com/bg/w?q={}&vst={}".format(input_,input_)
        
        # print(url,"\n","\n")

        html = requests.get(url=url)

        soup = BeautifulSoup(html.text, 'html.parser')

        next1 = soup.find_all(class_="product-card__titles")
        
        next2 = soup.find_all(class_="product-price css-11s12ax is--current-price")
        
        for elem in next1:
            self.titles.append(elem.get_text())
            self.size += 1

        for elem in next2:
            self.prices.append(elem.get_text())


        


