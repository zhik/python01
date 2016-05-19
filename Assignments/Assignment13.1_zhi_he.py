import urllib 
from bs4 import BeautifulSoup

url = raw_input("enter url: ")
if len(url) < 1 :
	url = "http://python-data.dr-chuck.net/comments_242237.html"
soup = BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')
nums = soup.find_all('span',{'class':'comments'})
print 'sum' , sum([int(i.get_text()) for i in nums]) , '\ncount' ,len(nums)