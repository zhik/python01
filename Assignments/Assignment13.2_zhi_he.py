import urllib 
from bs4 import BeautifulSoup

url = raw_input("enter start url: ")
count = int(raw_input("enter count/times: "))
position = int(raw_input("enter position: "))
if len(url) < 1 :
	url = "http://python-data.dr-chuck.net/known_by_Ross.html"

#run for count/time
for i in range(count):
	soup = BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')
	names = soup.find_all('a')
	urllist = []
	for name in names:
		#get the urls for that page
		urllist.append(str(name.get('href', None)))
	#change url at the position for next use
	url = urllist[position-1] 
	print "retrieving from:", url
print url, "is the answer"


