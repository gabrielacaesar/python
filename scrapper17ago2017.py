# my scrapper does work, but 
# the whole content is inside only one column

# we should have six columns; check the website

# we notice that the cells of the first column
# always have the class "sorting_1"


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://www.concursopublico.sp.gov.br/PortalConcurso/noauth/PortalDeConcursos.do?acao=concursoEncerrado"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

rows = [[td.text 
for td in tr.find_all('td')]
for tr in page_soup.find_all("tr")]

import csv
with open('concurso.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
