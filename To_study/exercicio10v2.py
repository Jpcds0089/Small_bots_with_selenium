from time import sleep
from datetime import datetime
from colorama import (Fore, Style)
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element

# CONFIGS

print(Fore.BLUE + "\nAbrindo navegador\n" + Style.RESET_ALL)
driver = Firefox()
waint = WebDriverWait(driver, 10, poll_frequency=1)
url = 'https://selenium.dunossauro.live/exercicio_10.html'

# INIT

# Indo para url
print(Fore.BLUE + "Indo para url\n" + Style.RESET_ALL)
driver.get(url)

# Preenchendo nome da tarefa
print(Fore.BLUE + "Preenchendo nome da tarefa\n" + Style.RESET_ALL)
input_nome = (By.ID, 'todo-name')
waint.until(visibility_of_element_located(input_nome), 'Elemento não visivel')
driver.find_element(*input_nome).send_keys('Acordar')

# Preenchendo descricão da tarefa
print(Fore.BLUE + "Preenchendo descricão da tarefa\n" + Style.RESET_ALL)
text_descricao = (By.CSS_SELECTOR, 'label[for="tarea"]')
input_descricao = (By.ID, 'todo-desc')
waint.until(text_to_be_present_in_element(text_descricao, 'Descrição da tarefa'), 'Elemento não tem o texto especificado')
driver.find_element(*input_descricao).send_keys('Toda manhã acordar 8 horas e ir lavar o rosto')

# Apertar em urgente
print(Fore.BLUE + "Apertando em urgente\n" + Style.RESET_ALL)
box = driver.find_element(By.ID, 'todo-next')
text_box = driver.find_element(By.CSS_SELECTOR, 'label ~ input[id="todo-next"]')
assert box.text == text_box.text
box.click()

# Apertar em colocar na fila
print(Fore.BLUE + "Apertando em colocar na fila\n" + Style.RESET_ALL)
button_colocar_na_fila = driver.find_element(By.ID, 'todo-submit')
assert button_colocar_na_fila.text == 'Colocar na Fila'
button_colocar_na_fila.click()

# Apertar em fazer (do)
print(Fore.BLUE + "Apertando em fazer (do)\n" + Style.RESET_ALL)
button_do = (By.CSS_SELECTOR, 'div[class="body_a"] div[class="buttons"]>button[class="btn btn-primary btn-ghost do"]')
waint.until(visibility_of_element_located(button_do))
button_do_text = driver.find_element(*button_do).text
assert button_do_text == 'Fazer'
driver.find_element(*button_do).click()

# Apertar em pronto (ready)
print(Fore.BLUE + "Apertando em pronto (ready)\n" + Style.RESET_ALL)
button_ready = (By.CSS_SELECTOR, 'div[class="body_b"] div[class="buttons"]>button[class="btn btn-primary btn-ghost do"]')
waint.until(visibility_of_element_located(button_ready))
button_ready_text = driver.find_element(*button_ready).text
assert button_ready_text == 'Pronto'
driver.find_element(*button_ready).click()

# Apertar em refazer (rebuild)
print(Fore.BLUE + "Apertando em refazer (rebuild)\n" + Style.RESET_ALL)
button_rebuild = (By.CSS_SELECTOR, 'div[class="body_c"] div[class="buttons"]>button[class="btn btn-primary btn-ghost do"]')
waint.until(visibility_of_element_located(button_rebuild))
button_rebuild_text = driver.find_element(*button_rebuild).text
assert button_rebuild_text == 'Refazer'
driver.find_element(*button_rebuild).click()

# Fechando driver
clock = str(datetime.now().time())[:8]
if 5 < int(clock[0]) <= 11:
    print(Fore.GREEN + "Automação finalizada. Tenha um bom dia!" + Style.RESET_ALL)
if 11 < int(clock[0]) <= 17:
    print(Fore.GREEN + "Automação finalizada. Tenha uma boa tarde!" + Style.RESET_ALL)
if 17 < int(clock[0]) <= 23 or -1 < int(clock[0]) <= 5:
    print(Fore.GREEN + "Automação finalizada. Tenha uma boa noite!" + Style.RESET_ALL)
sleep(5)
driver.quit()
