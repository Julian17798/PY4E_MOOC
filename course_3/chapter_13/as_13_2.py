import json
import ssl
from urllib.request import urlopen


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
if len(url) == 0: url = "http://py4e-data.dr-chuck.net/comments_42.json"
data = urlopen(url, context=ctx).read()

info = json.loads(data)

int_sum = 0

for item in info['comments']:
    int_sum += item['count']

print(f"Sum: {int_sum}")
