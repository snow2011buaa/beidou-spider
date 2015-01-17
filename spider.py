#encoding=utf-8

import urllib2
from bs4 import BeautifulSoup 

#To solve the encoding problem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('cars_meng0117.txt','w')

def getData(page):
	#The url is the core which is made up by analyse the request info of the web page
	url = '''http://cloud.bd56.com/cmsWebShowMoreOnlineTruck?targetUrl=CMSWEB/awbmoredata&pageNo=''' + page + '''&pageCount=109'''
	#url = '''http://cloud.bd56.com/cmsWebMoreOnlineGoods?targetUrl=CMSWEB/goodsSourceMoreData&pageNo=''' + page + '''&pageCount=36'''
	content = urllib2.urlopen(url).read()

	#the following code is to analyse the html text
	soup = BeautifulSoup(content)
	listString = soup.body.table.tr.td.ul

	itemList = listString.find_all('li')
	for item in itemList:
		ps = item.find_all('p')
		p = ps[2]
		title = p.get('title')
		title = title.replace(' ','')
		s = item.get_text().encode('utf-8').replace('\t','')
		s = s.replace(' ','')
		tokens = s.split()
		tokens[2] = title
		l = '\t'.join(tokens)
		#A wired 'space'
		f.write(l.replace('聽',''))
		f.write('\n')
	f.flush()

if __name__ == '__main__':
	for page in range(110):
		getData(str(page))
	f.close()
