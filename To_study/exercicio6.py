import string
import random
from time import sleep
from colorama import Fore
from colorama import Style
from selenium.webdriver import Firefox
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = Firefox()


# INIT---------------------------------------------------------------------------------------------------------------#


class Nome:

    def __init__(self):
        global in_loop
        print(Fore.GREEN + "\nAbrindo navegador\n" + Style.RESET_ALL)
        self.waint = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])

    def Start(self):
        driver.get("https://selenium.dunossauro.live/exercicio_06.html")
        self.PreencherFormulario()
        Quit()

    def PreencherFormulario(self):
        sleep(1)
        global in_loop
        in_loop = True
        for i in range(6):
            global selector, h2
            coluna = driver.find_element(By.CSS_SELECTOR, 'header > p > span').text
            if coluna == 'l0c0':
                h2 = 'form[class$=l0c0] h2'
                selector = 'form[class$=l0c0] input'
            elif coluna == 'l0c1':
                selector = 'form[class$=l0c1] input'
                h2 = 'form[class$=l0c1] h2'
            elif coluna == 'l1c0':
                h2 = 'form[class$=l1c0] h2'
                selector = 'form[class$=l1c0] input'
            elif coluna == 'l1c1':
                h2 = 'form[class$=l1c1] h2'
                selector = 'form[class$=l1c1] input'
            else:
                in_loop = False

            title = driver.find_element(By.CSS_SELECTOR, h2)
            print(Fore.BLUE + "Preenchendo", title.text + Style.RESET_ALL)
            self.EscreverComoPessoa(driver.find_element(By.CSS_SELECTOR, selector))
            self.EscreverComoPessoa(driver.find_elements(By.CSS_SELECTOR, selector)[1])
            driver.find_elements(By.CSS_SELECTOR, selector)[2].click()

    @staticmethod
    def EscreverComoPessoa(local):
        length_of_string = random.randint(8, 12)
        palavra = \
            ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        for letra in palavra:
            local.send_keys(letra)
            sleep(random.random() / 2.5)


def Quit():
    print(Fore.GREEN + "\nAutomacão concluida. Tenha um bom dia!" + Style.RESET_ALL)

    sleep(random.randint(2, 4))
    driver.quit()


bot = Nome()
bot.Start()


# Finish-------------------------------------------------------------------------------------------------------------#
