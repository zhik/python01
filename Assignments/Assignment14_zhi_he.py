import urllib
import xml.etree.ElementTree 

url = raw_input("enter url: ")
if len(url) < 1 :
	url = "http://python-data.dr-chuck.net/comments_242234.xml"
print 'sum' , sum([int(i.find('count').text) for i in xml.etree.ElementTree.parse(urllib.urlopen(url)).findall('comments/comment')])
