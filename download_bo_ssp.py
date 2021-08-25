from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# verificar se o chromedriver foi baixado na máquina
# verificar se o chromedriver é compatível com a versão do chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# informamos a url
url = "http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx"

# acessamos a url
driver.get(url)

# clique na aba FURTO DE CELULAR - ok/funciona
driver.find_element_by_link_text("FURTO DE CELULAR").click()

# clique no botão EXPORTAR - ok/funciona
driver.find_element_by_css_selector("button[id*='cphBody_ExportarBOLink']").click()

# demora para baixar
# acho que agora é criar loop com sleep()
