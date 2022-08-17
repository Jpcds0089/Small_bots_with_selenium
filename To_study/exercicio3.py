from time import sleep
from colorama import Fore
from colorama import Style
from urllib.parse import urlparse
from selenium.webdriver import Firefox
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



# INIT---------------------------------------------------------------------------------------------------------------#



class Exercicio:


    def __init__(self):

        print(Fore.BLUE + "Abrindo navegador" + Style.RESET_ALL)
        self.driver = Firefox()
        self.waint = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        self.driver.get("https://selenium.dunossauro.live/exercicio_03.html")
        sleep(1)


    def Start(self):
        self.Pagina0()
        self.Pagina1()
        self.Pagina2()
        self.Pagina3()
        self.Pagina4()


    def Pagina0(self):
        print(Fore.WHITE + " -Navegando pela page: 0" + Style.RESET_ALL)
        sleep(1)
        ancora_main = self.driver.find_element(By.TAG_NAME, "main")
        button_comecar_por_aqui = ancora_main.find_elements(By.TAG_NAME, "a")
        button_comecar_por_aqui[0].click()
        print(Fore.MAGENTA + " -Objetivo:0 concluido" + Style.RESET_ALL)


    def Pagina1(self):
        print(Fore.WHITE + " -Navegando pela page: 1" + Style.RESET_ALL)
        sleep(1)
        ancora_main = self.driver.find_element(By.TAG_NAME, 'main')
        ancora_li = ancora_main.find_elements(By.TAG_NAME, 'a')
        if ancora_li[0].get_attribute('attr') == 'errado':
            ancora_li[0].click()
        else:
            ancora_li[1].click()
        print(Fore.MAGENTA + " -Objetivo:1 concluido" + Style.RESET_ALL)


    def Pagina2(self):
        print(Fore.WHITE + " -Navegando pela page: 2" + Style.RESET_ALL)
        sleep(2)
        self.driver.refresh()
        sleep(20)
        title = self.driver.title
        ancora_main = self.driver.find_element(By.TAG_NAME, "main")
        resposta = ancora_main.find_elements(By.TAG_NAME, "a")
        if resposta[0].text == title:
            resposta[0].click()
        else:
            resposta[1].click()
        print(Fore.MAGENTA + " -Objetivo:2 concluido" + Style.RESET_ALL)


    def Pagina3(self):
        print(Fore.WHITE + " -Navegando pela page: 3" + Style.RESET_ALL)
        sleep(1)
        url = urlparse(self.driver.current_url)
        url_path = ''
        if url[2] == '/page_3.html':
            url_path = 'page_3.html'
        ancora_main = self.driver.find_element(By.TAG_NAME, "main")
        resposta = ancora_main.find_elements(By.TAG_NAME, "a")
        if resposta[0].text == url_path:
            resposta[0].click()
        else:
            resposta[1].click()
        print(Fore.MAGENTA + " -Objetivo:3 concluido" + Style.RESET_ALL)


    def Pagina4(self):
        sleep(1)
        self.driver.refresh()
        print(Fore.WHITE + " -Navegando pela page: 4" + Style.RESET_ALL)
        sleep(1)
        url_esperada = 'https://selenium.dunossauro.live/page_4.html'
        url = self.driver.current_url
        if url_esperada == url:
            print(Fore.MAGENTA + " -Objetivo:4 concluido" + Style.RESET_ALL)
            print(Fore.GREEN + "Parabens voce ganhou o desafio" + Style.RESET_ALL)
            sleep(5)
            self.driver.quit()
        else:
            print(Fore.RED + "Tente novamente" + Style.RESET_ALL)


    def find_by_text(self, browser, tag, text):

        elementos = browser.find_elements(By.TAG_NAME, tag)
        for elemento in elementos:
            if elemento.text == text:
                return elemento


    def find_by_ancora(self, browser, tag):
        elementos = browser.find_elements(By.TAG_NAME, tag)
        return elementos


bot = Exercicio()
bot.Start()


# Finish-------------------------------------------------------------------------------------------------------------#
