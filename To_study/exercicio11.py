from time import sleep
from random import randint
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element,\
    element_to_be_clickable, presence_of_element_located


# CONFIGS


def Escrever(loc, escrever):
    locator = (By.CSS_SELECTOR, loc)
    waint.until(element_to_be_clickable(locator))
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(escrever)


def Apertar(loc):
    locator = (By.CSS_SELECTOR, loc)
    waint.until(presence_of_element_located(locator))
    driver.find_element(*locator).click()


def Esperar(element,valor_atual, valor_desejado):
    count = 0
    loop = True
    while loop:
        sleep(0.5)
        count += 1
        if count <= 60:
            value_button = driver.find_element(By.CSS_SELECTOR, element).get_attribute(valor_desejado)
            if value_button != valor_atual:
                loop = False
            else:
                pass
        else:
            print('Tempo esgotado')
            driver.quit()


driver = Firefox()
waint = WebDriverWait(driver, 30, poll_frequency=1)
url = 'https://selenium.dunossauro.live/exercicio_11.html'

# INIT

# Indo para url
driver.get(url)
sleep(randint(1, 3))
driver.refresh()

# Escrevendo nome
Escrever('input[name="nome"]','Anonimo')

# Escrevendo email
Escrever('input[name="email"]', 'Email@email.email')

# Confirmando email
Escrever('input[name=c_email]', 'Email@email.email')

# Escrevendo senha
Escrever('input[name=senha]', 'minha senha 1 2 3')

# Confirmando senha
Escrever('input[name=c_senha]', 'minha senha 1 2 3')

# Apertando
Esperar('input[name="button"]', 'Bloqueado', 'value')
Apertar('input[name="button"]')
