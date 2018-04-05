from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib2


# Create your views here.

def home(request):
	url = "https://www.w3schools.com/html/html_tables.asp"

	resp = urllib2.urlopen(url)

	if resp.code == 200:
		html = resp.read()
		html_soup = BeautifulSoup(html, 'html.parser')
		print type(html_soup)
		m = html_soup.find_all('table', id = 'customers')
		# print type(m)
		# t = m[0].find_all('tr')
		# # l = []
		# # print t,"ooo"
		# for i in t[0:1]:
		# # 	print i,"kkkkk"
		# # 	l.append(i.th.text)

		# print l,"pppppppp"
	return HttpResponse(m)
	return render(request,'home.html',{'a':m})
