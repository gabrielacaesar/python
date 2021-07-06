from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://spotifycharts.com/regional/br/daily/2020-07-02')

botao = browser.find_element_by_class_name('header-csv')
botao.click()
