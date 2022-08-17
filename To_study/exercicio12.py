from time import sleep
from random import random
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
     element_to_be_clickable, presence_of_element_located, number_of_windows_to_be


# Functions----------------------------------------------------------------------------------------------------------#


def SwitchTo(driver, title_page:str):
    for window in driver.window_handles:
        driver.switch_to.window(window)
        if driver.title == title_page:
            break
    assert driver.title == title_page


def Click(driver, waint, loc_by_css_locator:str):
    locator = (By.CSS_SELECTOR, loc_by_css_locator)
    waint.until(presence_of_element_located(locator))
    driver.find_element(*locator).click()


def Write(driver, waint, tupla_locator:str, text:str):
    locator = tupla_locator
    waint.until(element_to_be_clickable(locator))
    driver.find_element(*locator).clear()
    for letra in text:
        driver.find_element(*locator).send_keys(letra)
        sleep(random() / 2.5)


# INIT---------------------------------------------------------------------------------------------------------------#


class Nome:


    def __init__(self):
        print("\nAbrindo navegador\n")
        self.driver = Firefox()
        self.alert = Alert(self.driver)
        self.waint = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.url = 'https://selenium.dunossauro.live/exercicio_12.html'
        self.nome = 'Anonimo'
        self.email = 'Email@email.email'
        self.signo = 'Tartaruga'

    def Start(self):
        self.driver.get(self.url)
        self.WriteNameEmailSigno()
        self.Send()
        self.Validation()
        self.Quit()

    def WriteNameEmailSigno(self):
        Click(self.driver, self.waint, 'input[name="nome"]')
        self.alert.send_keys(f'{self.nome}')
        self.alert.accept()

        Click(self.driver, self.waint, 'input[name="email"]')
        self.alert.send_keys(f'{self.email}')
        self.alert.accept()

        Click(self.driver, self.waint, 'input[name="signo"]')
        self.alert.send_keys(f'{self.signo}')
        self.alert.accept()

    def Send(self):
        Click(self.driver, self.waint, 'input[value="Enviar"]')

    def Validation(self):
        self.waint.until(number_of_windows_to_be(2))

        SwitchTo(self.driver, 'popup')
        print('Pagina atual:',self.driver.title)
        assert self.driver.title == 'popup'

        sleep(0.5)
        nome_obtido = self.driver.find_elements(By.TAG_NAME, 'h1')[1].text.replace('Nome: ', '')
        assert nome_obtido == self.nome, f'O nome obtido foi:"{nome_obtido}" E o nome verdadeiro e:"{self.nome}"'

        email_obtido = self.driver.find_elements(By.CSS_SELECTOR, 'h1')[2].text.replace('Email: ', '')
        assert email_obtido == self.email, f'O email obtido foi:"{email_obtido}" E o email verdadeiro e:"{self.email}"'

        signo_obtido = self.driver.find_elements(By.CSS_SELECTOR, 'h1')[3].text.replace('Signo: ', '')
        assert signo_obtido == self.signo, f'O signo obtido foi:"{signo_obtido}" E o signo verdadeiro e:"{self.signo}"'

    def Quit(self):
        print("\nAutomacão concluida. Tenha um bom dia.")

        sleep(2)
        self.driver.quit()


bot = Nome()
bot.Start()


# Finish-------------------------------------------------------------------------------------------------------------#
