from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import *
import selenium
import time
from selenium.webdriver.chrome.options import Options


website = 'https://www.xbox.com/pt-BR/live'


class validationXboxLive():
    def __init__(self, email, password):

        self.email = email
        self.password = password
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.set_window_position(1024, 600)
        self.browser.maximize_window()
        self.browser.get(website)
        self.browser.implicitly_wait(2)

        # aceitando os cookies
        self.browser.find_element(
            By.XPATH, value='//*[@id="wcpConsentBannerCtrl"]/div[2]/button[1]').click()
        self.browser.implicitly_wait(2)

        # sing-in
        self.browser.find_element(
            By.XPATH, value='//*[@id="mectrl_headerPicture"]').click()
        self.browser.implicitly_wait(2)

        # inserir o email
        self.browser.find_element(
            By.CSS_SELECTOR, value='#i0116').send_keys(self.email)
        self.browser.implicitly_wait(2)

        #botão: próximo
        self.browser.find_element(By.ID, value='idSIButton9').click()
        self.browser.implicitly_wait(4)

        # inserir a senha
        self.browser.find_element(
            By.XPATH, value='//*[@id="i0118"]').send_keys(self.password)
        self.browser.implicitly_wait(4)

        #botao: entrar
        self.browser.find_element(
            By.XPATH, value='/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').click()
        self.browser.implicitly_wait(2)

        #botão: sim manter conectado
        self.browser.find_element(
            By.ID, value='idSIButton9').click()
        self.browser.implicitly_wait(2)

        #botão do avatar (lado direito superior)
        self.browser.find_element(
            By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div/header/div/div/div[4]/div[2]/div/div/button/div/div').click()
        self.browser.implicitly_wait(2)

        #botao Xbox Perfil
        self.browser.find_element(By.XPATH, value= '/html/body/div[1]/div/div/div[2]/div/div/div/header/div/div/div[4]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[4]/a').click()
        self.browser.implicitly_wait(2)

        #pesquisa do campo encontrar pessoas ou club
        self.browser.find_element(By.XPATH, value='/html/body/app/core-page/div/section[2]/core-area/core-region-pivot/section/section/section/div/div/rendermodule/div/xbox-friends/div/div[1]/xbox-search/form/input').send_keys('Player Micky')       
        time.sleep(2)

        #botão de pesquisa
        self.browser.find_element(By.XPATH, value='html/body/app/core-page/div/section[2]/core-area/core-region-pivot/section/section/section/div/div/rendermodule/div/xbox-friends/div/div[1]/xbox-search/form/button[1]').click()     
        time.sleep(2)


       

email = 'ramon.basilio@hotmail.com'
password = 'Gta5632bv'

myAutomationWeb = validationXboxLive(email, password)
