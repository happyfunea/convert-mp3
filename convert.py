#!/usr/bin/python2.7.x
#-*-coding:utf-8-*-

try:
	import requests
        import subprocess as a
	import urllib, threading
	import sys, time as molor
	import re, logging
	import mechanize
except ImportError as bebek:
	print bebek
	sys.exit

class lagu:
	global output
	url = 'http://www.convertmp3.io/'
	def __init__(self, link):
		
		try:
			self.br = mechanize.Browser()
			self.br.set_handle_robots(False)
			self.br.set_handle_referer(True)
			self.br.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0')]
			self.br._factory.is_html = (True)
			self.br.open(lagu.url)
			self.br.select_form(nr=0)
			self.br.form['video'] = link
			self.br.submit()
			self.get = self.br.geturl()
			self.rekues = requests.get(self.get)
			self.reg = re.findall(r'href="/download(.*?)">', self.rekues.text)
			self.cek = re.findall(r'<title>(.*?)</title>', self.rekues.text)
			self.title = re.findall(r'id="videoTitle">(.*?)</span>', self.rekues.text)
		except Exception as a:
			logging.error(a)
			sys.exit
		
	def donlot(self, output):
		try:
			logging.warning(' Title Music : {}'.format(self.title[0]))
			if 'Your MP3 Is Ready' in self.cek[0]:
				print 'STATUS | Loading For Download'
				self.gut = requests.get('http://www.convertmp3.io/download{}'.format(self.reg[0]))
				self.bat = urllib.urlretrieve(self.gut.url, output+'.mp3')
				print 'STATUS | (S)uccess!!\nOUTPUT | {}'.format(output+'.mp3')
			elif 'No video was found' in self.title[0]:
				logging.error( '(T)idak Di Temukan')
				sys.exit()
			else:
				logging.error( '(A)borted!')
				sys.exit()
		except Exception as sayang:
			logging.error(sayang)
			sys.exit() 
def banner():
	baner = '''\t                         #              ### 
\t### ### ##  # # ### ### ###     ### ###   # 
\t#   # # # # # # ##  #    #      ### # #  ## 
\t### ### # #  #  ### #    ##     # # ###   # 
\t                                    #   ###
         AUTHOR : (A)gung
         CONTACT : (https://t.me/Agung_sp1)
         TEAM : (407(AEX)) & (CRABS)\n''';print baner
try:
	if __name__=='__main__':
                a.call('clear', shell=True)
		banner()
		out = sys.argv[2]
		syes = sys.argv[1]
		bang = lagu(syes)
		bang.donlot(out)
except IndexError:
	print 'Ex : python2 yt.py <url yutub> <output>'
	sys.exit()
