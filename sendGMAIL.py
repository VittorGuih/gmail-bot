import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

gmail_url = 'https://gmail.com'
destinatario = ' EMAIL DO DESTINATARIO'


firefox_profile = webdriver.FirefoxProfile('CAMINHO PARA O PROFILE DESEJADO')
driver = webdriver.Firefox(firefox_profile)
driver.get(gmail_url)

# Tempo para carregar o link
time.sleep(3)

# Clicar no botão de enviar mensagem
btn_escrever = driver.find_element_by_class_name('z0')
btn_escrever.click()

# Tempo para carregar caixa de escrita
time.sleep(10)

# Adicionar os destinatários da mensagem
campo_destinatario = driver.find_element_by_class_name('vO')
campo_destinatario.click()
campo_destinatario.send_keys(destinatario)
campo_destinatario.send_keys(Keys.ENTER)

# Inserir o assunto
campo_assunto = driver.find_element_by_class_name('aoT')
campo_assunto .click()
campo_assunto .send_keys('Testing')

time.sleep(1)
# Inserir mensagem principal
xpth = '/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[' \
       '4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div '

# Condição da seleção do elemento
if driver.find_element_by_xpath(xpth):
    campo_mesagem_principal = driver.find_element_by_xpath(xpth)
else:
    campo_mesagem_principal = driver.find_element_by_id(':pz')
campo_mesagem_principal.click()
campo_mesagem_principal.send_keys('Testing')
