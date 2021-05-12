from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
if len(url) == 0: url = "http://py4e-data.dr-chuck.net/comments_42.xml"
xml = urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)

int_sum = 0

for element in tree.findall('.//count'):
    try:
        int_sum += int(element.text)
    except:
        pass

print(f"Sum: {int_sum}")
