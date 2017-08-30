#learning web scraping with @duarteguilherme, data editor at JOTA

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

banco = MongoClient().presidente.agenda

class Crawler:
    def __init__(self):
        self.url = "http://www2.planalto.gov.br/acompanhe-planalto/agenda-do-presidente/agenda-do-presidente-michel-temer/2017-"
        self.headers = {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2",
                "Connection":"keep-alive",
                "Host":"www2.planalto.gov.br",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
                }
        for i in range(1,8):
            for j in range(1,32):
                url = self.url + "{0:02d}-".format(i) + "{0:02d}".format(j)
                print(url)
                self.baixa_pagina(url)
       
    def baixa_pagina(self,url):
        pagina = requests.get(url, headers=self.headers).text
        sopa = BeautifulSoup(pagina, "html.parser")
        compromissos = sopa.find_all('li', attrs={'class':'item-compromisso'})
        dicio_dados = {}
        if 'Sem compromissos oficiais' in sopa.text:
            print("Sem compromisso")
            return False
        arquivo = open('agenda.csv','a')
        for i in compromissos:
            dicio_dados['data_hora'] = i.find('time')['datetime']
            dicio_dados['titulo'] = i.find('h4').text
            try:
                dicio_dados['local'] = i.find('p').text
            except:
                pass
            print(dicio_dados)
            for j in dicio_dados:
                arquivo.write('"' + dicio_dados[j] + '",')        
            arquivo.write('\n')
        arquivo.close()


x = Crawler()