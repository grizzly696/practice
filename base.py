import os
import requests
from bs4 import BeautifulSoup
print(os.system("cat /etc/passwd"))
url ="https://market.yandex.ru"

req = requests.get(url)
tml = req.text
print(tml)
