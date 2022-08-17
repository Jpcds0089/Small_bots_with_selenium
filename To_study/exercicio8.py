from time import sleep
from colorama import Fore
from colorama import Style
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = Firefox()


# INIT---------------------------------------------------------------------------------------------------------------#


class Nome:

    def __init__(self):
        print(Fore.GREEN + "\nAbrindo navegador\n" + Style.RESET_ALL)
        driver.get('https://selenium.dunossauro.live/caixinha')

    def Start(self):
        self.LocBox()
        self.SetClolorsBox(loc_box, loc1=loc_span)
        self.SetClolorsBox(loc_box, loc_span, Keys.SHIFT)
        self.SetClolorsBox(loc_box, loc_span, Keys.CONTROL)
        self.SetClolorsBox(loc_box, loc_span, key=Keys.SHIFT, key1=Keys.CONTROL)
        #self.Quit()

    def LocBox(self):
        sleep(1)
        global loc_box, loc_span
        loc_box = driver.find_element(By.ID, 'caixa')
        loc_span = driver.find_element(By.TAG_NAME, 'span')

    def SetClolorsBox(self, loc, loc1=None, key=None, key1=None):
        ac = ActionChains(driver)
        ac.pause(1)

        if key:
            ac.key_down(key)
        if key1:
            ac.key_down(key1)

        ac.move_to_element(loc)
        ac.pause(1)
        ac.click(loc)
        ac.pause(1)
        ac.double_click(loc)

        if key is None and key1 is None:
            ac.pause(1)
            ac.context_click(loc)

        if loc1:
            ac.pause(1)
            ac.move_to_element(loc1)

        if key:
            ac.key_up(key)
        if key1:
            ac.key_up(key1)

        ac.perform()
        sleep(0.5)
        self.GetColors()
        sleep(0.5)
        driver.refresh()
        sleep(0.5)
        self.LocBox()

    def GetColors(self):
        # Init
        resultados_dos_eventos = driver.find_element(By.TAG_NAME, 'textarea').text
        list_resultado = resultados_dos_eventos.split('\n')
        list_colors_disorganized = []
        list_colors_organized = []
        list_colors = []

        # Pegar cores do resultado
        for resultado in list_resultado:
            colors_desorganized = resultado.split(',')[1]
            list_colors_disorganized.append(colors_desorganized)

        # Organizar cores
        list_colors_organized = set(list_colors_disorganized)
        list_colors_organized = list(set(list_colors_disorganized))

        # Mostrar cores organizadas sem as '""'(aspas) e o ' '(espaco)
        print(' ')
        for color in list_colors_organized:
            cor = color.replace('\"', '')
            cor = cor.replace(' ', '')
            list_colors.append(cor)
            print(cor)

    def Quit(self):
        print(Fore.GREEN + "\nAutomacão concluida. Tenha um bom dia." + Style.RESET_ALL)
        sleep(5)
        driver.quit()


bot = Nome()
bot.Start()

# Finish-------------------------------------------------------------------------------------------------------------#
