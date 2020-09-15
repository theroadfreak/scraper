# import requests
# from bs4 import BeautifulSoup
from csv import writer
from buzz import buzz

in_ = input('ime: ')
buzz = buzz(in_)

for n in range(buzz.size):
    print(buzz.titles[n],'    ',buzz.prices[n])
    print('_________________________________________________________________________')

