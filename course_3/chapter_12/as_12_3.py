from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def executeCycle(link, c, p):
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    result = tags[p].get('href', None)
    print(result)

    if c > 0:
        executeCycle(result, c - 1, p)


url = input("Enter url: ")
count = int(input("Enter count: ")) - 1
position = int(input("Enter position: ")) - 1

if len(url) == 0: url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

executeCycle(url, count, position)
