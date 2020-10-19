import sys, requests

url = sys.argv[1]
if url == "http://localhost:5100":
    keydict = requests.get(url).json()
    keyList = keydict["keys"]
    for key in keyList:
        values = requests.get(url + '/' + key).json()
        print(str(values))