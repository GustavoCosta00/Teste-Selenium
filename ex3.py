from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(4)

linguagem = navegador.find_element('xpath','//*[@id="langSelect-PT-BR"]').click()

time.sleep(4)

elemento = navegador.find_element('xpath','//*[@id="bigCookie"]')

action = ActionChains(navegador)


def cont_cookies():
    limit = 5000
    start = 1
    while( start < limit):
        action.move_to_element(elemento).click().perform()
        start = start + 1
        time.sleep(0.01)

cont_cookies()
