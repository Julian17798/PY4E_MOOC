import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input("Enter location: ")
    params = {'address': address, 'key': 42}
    url = api_url + urllib.parse.urlencode(params)

    data = urllib.request.urlopen(url, context=ctx).read().decode()
    try:
        js = json.loads(data)
    except:
        print("Something went wrong")
        continue

    print(json.dumps(js, indent=4))

