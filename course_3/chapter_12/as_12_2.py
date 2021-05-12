from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
if len(url) == 0: url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

int_sum = 0

# Retrieve all of the span tags
tags = soup.findAll("span")
for tag in tags:
    try:
        int_sum += int(tag.contents[0])
    except:
        pass

print(f"Sum: {int_sum}")
