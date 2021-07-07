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
  #evento_tipo_n = []
  link_n = []
  indice_n = []
  dados_n = []

  eventos = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  data = browser.find_elements_by_xpath('//span[@class="g-agenda__data"]')
  hora = browser.find_elements_by_xpath('//span[@class="g-agenda__hora"]')
  local = browser.find_elements_by_xpath('//span[@class="g-agenda__categoria"]')
  evento = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  #evento_tipo = browser.find_elements_by_xpath('//span[@class="g-agenda__tipo"]')
  link = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  
  for i in range(0, len(eventos)):
    data_2 = data[i].text
    hora_2 = hora[i].text
    local_2 = local[i].text
    evento_2 = evento[i].text
    #evento_tipo_2 = evento_tipo[i].text
    link_2 = link[i].get_attribute("href")
    indice = i
  
    data_n.append(data_2)
    hora_n.append(hora_2)
    local_n.append(local_2)
    evento_n.append(evento_2)
    #evento_tipo_n.append(evento_tipo_2)
    link_n.append(link_2)
    indice_n.append(indice)
    print('Entrando aqui/n \n')
    print(indice, data_2, hora_2, local_2, evento_2, link_2)	

    dados = {'data' : [data_n], 'hora' : [hora_n], 'local' : [local_n], 'evento' : [evento_n], 'link' : [link_n]}
    dados_n.append(dados)

#print(data_n, hora_n, local_n, evento_n, evento_tipo_n, link_n)
