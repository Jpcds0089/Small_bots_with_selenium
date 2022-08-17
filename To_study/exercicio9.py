from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Configs------------------------------------------------------------------------------------------------------------#


driver = Firefox()
waint = WebDriverWait(driver, 10, poll_frequency=1)


class WaintPageLoadConfig:
    def __init__(self, locate):
        self.loc = locate

    def __call__(self, webdriver):
        elements = webdriver.find_elements(*self.loc)
        if elements:
            return 'terminal-alert terminal-alert-error' in elements[0].get_attribute('class')
        return False


def Quit():
    print("\nAutomacão concluida. Tenha um bom dia.")
    sleep(5)
    driver.quit()


# INIT---------------------------------------------------------------------------------------------------------------#


class Nome:

    def __init__(self):
        print("\nAbrindo navegador\n")
        driver.get('https://selenium.dunossauro.live/exercicio_09.html')
        self.loc_waint_page_load = (By.CSS_SELECTOR, 'div[class$=terminal-alert-error]')
        self.loc_button = (By.NAME, 'button')

    def Start(self):
        self.FindButton()
        Quit()

    def FindButton(self):
        global class_button
        try:
            waint.until_not(WaintPageLoadConfig(self.loc_waint_page_load))
        except:
            pass
        count1 = 0
        count2 = 0
        count3 = 0
        loop = True
        while loop:
            try:
                button = driver.find_element(By.NAME, 'button')
                class_button = button.get_attribute("class")
            except:
                pass
            if class_button == 'btn btn-primary btn-ghost':
                count1 += 1
                count2 = 0
                count3 = 0
                if count1 == 1:
                    print(f'Class do botão "pyimary"')
            elif class_button == 'btn btn-default btn-ghost':
                count1 = 0
                count2 += 1
                count3 = 0
                if count2 == 1:
                    print(f'Class do botão "default"')
            elif class_button == 'btn btn-error btn-ghost':
                count1 = 0
                count2 = 0
                count3 += 1
                if count3 == 1:
                    print(f'Class do botão "error"')


bot = Nome()
bot.Start()

# Finish-------------------------------------------------------------------------------------------------------------#
