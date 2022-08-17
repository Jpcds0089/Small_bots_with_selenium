from time import sleep
from colorama import Fore
from colorama import Style
from random import randint
from selenium.webdriver import Firefox
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



# INIT---------------------------------------------------------------------------------------------------------------#



class Nome:


    def __init__(self):
        print(Fore.BLUE + "Abrindo navegador" + Style.RESET_ALL)
        self.driver = Firefox()
        self.waint = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])


    def Start(self):
        self.driver.get("https://curso-python-selenium.netlify.app/exercicio_02.html#")
        self.Jogando()

    def Jogando(self):
        sleep(1)
        print(Fore.MAGENTA + "Jogando" + Style.RESET_ALL)
        in_running = True
        while in_running:

            sleep(randint(1, 2))
            print(Fore.YELLOW + " Tentando novamente" + Style.RESET_ALL)
            button_click = self.driver.find_elements(By.TAG_NAME, 'a')
            button_click[0].click()

            condicao = self.driver.find_elements(By.TAG_NAME, 'p')
            if condicao[-1].text == 'você está fazendo algo errado':
                print(Fore.GREEN + "Parabens voce ganhou!" + Style.RESET_ALL)
                sleep(3)
                self.driver.quit()
                in_running = False



bot = Nome()
bot.Start()


# Finish-------------------------------------------------------------------------------------------------------------#
