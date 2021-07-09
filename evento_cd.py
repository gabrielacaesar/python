from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())

url_list = list(map('https://www.camara.leg.br/agenda/?dataInicial__proxy=18/03/2020&dataInicial=18/03/2020&dataFinal__proxy=06/07/2021&dataFinal=06/07/2021&categorias=Plen%C3%A1rio&pagina={}'.format, range(1, 6)))

data_n = []
hora_n = []
local_n = []
evento_n = []
link_n = []
indice_n = []
dados_n = []
url_n = []

for n in range(0,len(url_list)):
  browser.get(url_list[n])
  
  eventos = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  data = browser.find_elements_by_xpath('//span[@class="g-agenda__data"]')
  hora = browser.find_elements_by_xpath('//span[@class="g-agenda__hora"]')
  local = browser.find_elements_by_xpath('//span[@class="g-agenda__categoria"]')
  evento = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  link = browser.find_elements_by_xpath('//a[@class="g-agenda__nome"]')
  
  for i in range(0, len(eventos)):
    data_n.append(data[i].text)
    hora_n.append(hora[i].text)
    local_n.append(local[i].text)
    evento_n.append(evento[i].text)
    link_n.append(link[i].get_attribute("href"))
    indice_n.append(i)
    url_n.append(url_list[n])

dados = {'data' : data_n, 'hora' : hora_n, 'local' : local_n, 'evento' : evento_n, 'link' : link_n, 'url' : url_n}

df = pd.DataFrame(dados)
browser.quit()

# padronizacao da coluna, filtro por deliberativa e por link do portal da cd
df['evento'] = df['evento'].str.upper().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
filtro_evento = df['evento'].str.contains("SESSAO DELIBERATIVA")
filtro_link = df['link'].str.contains("camara.leg.br")

df2 = df.loc[filtro_evento]
sessao_deliberativa = df2.loc[filtro_link]

#sessao_deliberativa.to_csv('dados_n.csv', encoding='utf-8', index = False)

url_deliberativa = sessao_deliberativa['link']

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url_deliberativa[1])



