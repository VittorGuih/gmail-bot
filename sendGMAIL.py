import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

gmail_url = 'https://gmail.com'
destinatario = 'YOUR EMAIL'
mensagem_principal = 'Testing Main Message Field'
subject_field = 'Subject Testing'

# Variavel do Profile
mozilla_profile = 'YOUR BROWSER PATH'

# Variaveis de elemento
id_main_message_field = ':pz'
class_name_btn_escrever = 'z0'
class_name_destinatario_field = 'vO'
class_name_assunto_field = 'aoT'

firefox_profile = webdriver.FirefoxProfile(mozilla_profile)
driver = webdriver.Firefox(firefox_profile)
driver.get(gmail_url)

# Tempo para carregar o link
time.sleep(3)

# Clicar no botão de enviar mensagem
btn_escrever = driver.find_element_by_class_name(class_name_btn_escrever)
btn_escrever.click()

# Tempo para carregar caixa de escrita
time.sleep(10)

# Adicionar os destinatários da mensagem
campo_destinatario = driver.find_element_by_class_name(class_name_destinatario_field)
campo_destinatario.click()
campo_destinatario.send_keys(destinatario)
campo_destinatario.send_keys(Keys.ENTER)

# Inserir o assunto
campo_assunto = driver.find_element_by_class_name(class_name_assunto_field)
campo_assunto.click()
campo_assunto.send_keys(subject_field)

time.sleep(1)

# Inserir mensagem principal
campo_mensagem_principal = driver.find_element_by_id(id_main_message_field)
campo_mensagem_principal.click()
campo_mensagem_principal.send_keys(mensagem_principal)




# anexo = driver.find_element_by_xpath('/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[4]/div/div[1]/div/div/div')
# anexo.click()
# anexo.send_keys("C:\\Users\\vitto\\Documents\\Front-End\\Selenium\\gmail-message-bot\\test.png")

# Forma de encontrar o id dinamico de uma classe, usando o seletor do CSS
# input_tag = driver.find_element_by_css_selector('div.Am.Al.editable.LW-avf.tS-tW')
# input_tag = input_tag.get_attribute('id')

# Outra opção para encontrar o elemento do campo de texto onde a mensagem principal é inserida (não funciona em todos os navegadores)
# full_path_message_area = '/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[' \
#       '4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div'

# campo_mensagem_principal = driver.find_element_by_xpath(full_path_message_area)
