# código retirado do repositório 'treinamento' de @fmasanori
# fiz comentários para entender e rodar o código
# a raspagem é dos salários de funcionários da USP
# coda.br, em 25 de novembro
from bs4 import BeautifulSoup as bs
import requests
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

u = 'https://uspdigital.usp.br/portaltransparencia/portaltransparenciaListar?paginar=s&dtainictc=01%2F10%2F2017&nompes=&nomundorg=&nomdepset=&tipcon=&tipcla=&nomabvfnc=&Submit=Solicitar+pesquisa&reload=buscar&imagem=S&print=true&chars=4b9k&pag='
teto = 21631.05
for k in range(1, 856):
  print (f'Página {k}')
  saida = open('SálariosUSP.txt', 'a')
  p = requests.get(u+str(k))
  s = bs(p.content, 'html.parser')
  t = s.find('table', {'class':'table_list'})
  f = t.findAll('tr')
  for x in f[1:]:
  # significa que eu quero do 1 até o final
    tds = x.findAll('td')
    nome = tds[0].string
    função = tds[-6].string
    tempoUsp = tds[-4].string
    salário = tds[-2].string
  # -2 significa penúltida, contagem funciona de trás para frente
    salário = locale.atof(salário)
    if salário > teto:
      saida.write(','.join([nome, função, tempoUsp, str(salário)]) + '\n')
  saida.close()
