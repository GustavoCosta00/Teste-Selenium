# CONFIGURANDO O AMBIENTE
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as ky
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get('https://www.recepedia.com/pt-br/artigos/7-receitas-de-bolo-usando-ingredientes-que-voce-tem-em-casa/')


try:
    main = WebDriverWait(navegador,10).until(
        EC.presence_of_element_located((By.ID,'content'))
    )
    print("Funcionando")


    titles = main.find_elements(By.TAG_NAME,'h3')
    for title in titles:
        print(title.text)

    
finally:
    navegador.quit()
    
    """
        UMA FORMA DE LIMITAR O NÚMERO DE REPETIÇÕES DESSE LADO É DA SEGUINTE FORMA:
        
        limite = 7

        for indice, title in enumerate(titles):

        if indice >= limite:
            break  
        print(title.text)
    """

time.sleep(3)

navegador.quit()

