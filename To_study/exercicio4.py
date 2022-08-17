from time import sleep
from json import loads
from colorama import Fore
from colorama import Style
from datetime import datetime
from urllib.parse import urlparse
from random import random, randint
from selenium.webdriver import Firefox
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# INIT---------------------------------------------------------------------------------------------------------------#


class Bot:
    def __init__(self):
        self.driver = Firefox()
        print(Fore.GREEN + "\nAbrindo navegador\n" + Style.RESET_ALL)
        self.waint = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[
            NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        self.formulario = {"nome": "Anonimo",
                           "email": "email@email.com",
                           "senha": "minhasenha1234",
                           "telefone": "123456789"}

    def Start(self):
        self.driver.get("https://selenium.dunossauro.live/exercicio_04.html")
        self.PreencherFormulario(self.driver, **self.formulario)
        self.comparar_se_texto_pagina_igual_url()
        self.Quit()

    def PreencherFormulario(self, browser, nome, email, senha, telefone):
        print(Fore.BLUE + "Preenchendo formulario..." + Style.RESET_ALL)
        sleep(2)
        self.EscreverComoPessoa(browser.find_element(By.NAME, "nome"), nome)
        sleep(random())
        self.EscreverComoPessoa(browser.find_element(By.NAME, "email"), email)
        sleep(random())
        self.EscreverComoPessoa(browser.find_element(By.NAME, "senha"), senha)
        sleep(random())
        self.EscreverComoPessoa(browser.find_element(By.NAME, "telefone"), telefone)
        sleep(random())
        browser.find_element(By.NAME, "btn").click()

    def comparar_se_texto_pagina_igual_url(self):
        sleep(2)
        # Url page
        # logic
        current_url = urlparse(self.driver.current_url)
        query_url = current_url.query.split("&")
        resp_query_1 = query_url[0].split("=")
        resp_query_2 = query_url[1].split("=")
        resp_query_3 = query_url[2].split("=")
        resp_query_4 = query_url[3].split("=")

        # List
        name = resp_query_1[0]
        resp_name = resp_query_1[1]
        email = resp_query_2[0]
        resp_email = resp_query_2[1].replace("%", "@").replace("4", "").replace("0", "")
        senha = resp_query_3[0]
        resp_senha = resp_query_3[1]
        telefone = resp_query_4[0]
        resp_telefone = resp_query_4[1]

        newl = {
            name: resp_name,
            email: resp_email,
            senha: resp_senha,
            telefone: resp_telefone
        }
        # Text page
        main = self.driver.find_element(By.ID, "main").find_element(By.TAG_NAME, "textarea")
        main_arrumado = loads(main.text.replace('\'', "\""))
        assert main_arrumado == newl

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

    @staticmethod
    def EscreverComoPessoa(local, palavra):
        for letra in palavra:
            local.send_keys(letra)
            sleep(random() / 2)


bot = Nome()
bot.Start()


# Finish-------------------------------------------------------------------------------------------------------------#
