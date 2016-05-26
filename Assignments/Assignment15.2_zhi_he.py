import urllib
import json

url = raw_input("enter url: ")
if len(url) < 1 :
    url = "http://python-data.dr-chuck.net/comments_242238.json"

data = urllib.urlopen(url).read()
js = json.loads(str(data))

print 'count:' , len(js["comments"]), '\nsum: ', sum([int(i["count"]) for i in js["comments"]])