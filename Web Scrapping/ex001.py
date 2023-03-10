from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

os.system('cls')



html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)