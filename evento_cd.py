from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())

url_list = list(map('https://www.camara.leg.br/agenda/?dataInicial__proxy=18/03/2020&dataInicial=18/03/2020&dataFinal__proxy=06/07/2021&dataFinal=06/07/2021&categorias=Plen%C3%A1rio&pagina={}'.format, range(1, 11)))

for n in range(0, len(url_list)):
  browser.get(url_list[n])
  print(url_list[n])
  
  data_n = []
  hora_n = []
  local_n = []
  evento_n = []
  evento_tipo_n = []
  link_n = []
  indice_n = []
  dados_n = []

  eventos = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')

  for i in range(0, len(eventos)):
    data = browser.find_element_by_xpath('//span[@class="g-agenda__data"]').text
    hora = browser.find_element_by_xpath('//span[@class="g-agenda__hora"]').text
    local = browser.find_element_by_xpath('//span[@class="g-agenda__categoria"]').text
    evento = browser.find_element_by_xpath('//a[@class="g-agenda__nome"]').text
    evento_tipo = browser.find_element_by_xpath('//span[@class="g-agenda__tipo"]').text
    link = browser.find_element_by_xpath('//a[@class="g-agenda__nome"]').get_attribute("href")
    indice = i
  
    data_n.append(data)
    hora_n.append(hora)
    local_n.append(local)
    evento_n.append(evento)
    evento_tipo_n.append(evento_tipo)
    link_n.append(link)
    indice_n.append(indice)

#print(data_n, hora_n, local_n, evento_n, evento_tipo_n, link_n)
#print(data, hora, local, evento, evento_tipo, link)

    dados = {'data' : [data_n], 'hora' : [hora_n], 'local' : [local_n], 'evento' : [evento_n],
'evento_tipo' : [evento_tipo_n], 'link' : [link_n]}
    dados_n.append(dados)
