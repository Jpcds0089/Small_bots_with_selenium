from time import sleep
from colorama import Fore
from colorama import Style
from random import randint
from datetime import datetime
from selenium.webdriver import Firefox
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



# INIT---------------------------------------------------------------------------------------------------------------#



class Bot:
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
                self.Quit()
                in_running = False

    def Quit(self):
        clock = str(datetime.now().time())[:8]
        if 5 < int(clock[0]) <= 11:
            print(Fore.GREEN + "Automação finalizada. Tenha um bom dia!" + Style.RESET_ALL)
        if 11 < int(clock[0]) <= 17:
            print(Fore.GREEN + "Automação finalizada. Tenha uma boa tarde!" + Style.RESET_ALL)
        if 17 < int(clock[0]) <= 23 or -1 < int(clock[0]) <= 5:
            print(Fore.GREEN + "Automação finalizada. Tenha uma boa noite!" + Style.RESET_ALL)
        sleep(randint(1, 2 + randint(1, 3)))
        self.driver.quit()


bot = Bot()
bot.Start()


# Finish-------------------------------------------------------------------------------------------------------------#
