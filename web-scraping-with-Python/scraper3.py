from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://projetoplenario.com/reforma-trabalhista.html")
bsObj = BeautifulSoup(html)

namelist = bsObj.findAll("p", {"class":"senadoresName"})
for name in namelist:
	print(name.get_text()) 
	#get_text() remove as tags do coumento e retorna string