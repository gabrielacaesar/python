#reaproveitamento do código raspa03 para solucionar problema
#em que queremos analisar os gastos com a Copa de 2014
from urllib.request import urlopen
from bs4 import BeautifulSoup

xml = urlopen("http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento")
#na linha superior, trocamos o nome da variável para fazer mais sentido
#antes, a var se chamava html e agora recebe o nome xml
bsObj = BeautifulSoup(xml, "xml") #indicamos o formato do arquivo que estamos lendo
valores = bsObj.findAll("valorTotalPrevisto")
#trocamos o nome nameList para valores, assim faz mais sentido
#trocamos name por 'v', pelo mesmo motivo
total = 0
for v in valores:
    print(v.string)
    total = total + float(v.string)

print(total)
