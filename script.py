from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import keyboard
from time import sleep


#caminho do driver do edge
service = Service(r"C:\User\stari\Downloads\edgedriver_win64\msedgedriver.exe")
#inicia o driver do edge
driver = webdriver.Edge(service=service)

#deixa a janela maximizada
driver.maximize_window()

#entra em uma pagina
driver.get("https://ofertasmateus.com/")

pyautogui.click(1241,375)

#espera o site o carregar
WebDriverWait(driver,10).until(
    lambda d: d.execute_script('return document.readyState') == 'complete'
)

print("Página carregada com sucesso")


#aceita cookies caso tenha
try:
    cookies = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@aria-label= "Aceitar"]'))
    )
    cookies.click()
    print('Cookies Aceitos')
except:
    print('Cookies não encontrado')



elemento_estado = driver.find_element(By.CLASS_NAME, 'search')
elemento_estado.click()

pyautogui.moveTo(501,473)


sleep(1)

pyautogui.scroll(-200)

estado = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[2]/div/div[2]/div/div[2]/div[8]')
sleep(1)
estado.click()


elemento_cidade = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[2]/div/div[2]/div[2]/input')
elemento_cidade.click()


cidade = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[2]/div/div[2]/div[2]/div[2]/div[4]')
sleep(1)
cidade.click()


elemento_loja = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[2]/div/div[2]/div[3]/input')
elemento_loja.click()

loja = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[2]/div/div[2]/div[3]/div[2]/div[2]')
sleep(1)
loja.click()


menus = driver.find_elements(By.CLASS_NAME, "menu")

menu_encarte = menus[3]

elemento_encarte = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[2]/div/div[2]/div[4]/input')
elemento_encarte.click()

itens = menu_encarte.find_elements(By.CLASS_NAME, 'item')

data_values = []

for item in itens:
    data_values.append(item.get_attribute('data-value'))


ultimo_valor = data_values[-1]

for data in data_values:
    xpath = f"//div[@data-value = '{data}']"
    driver.find_element(By.XPATH, xpath).click()

    sleep(2)

    pyautogui.hotkey('ctrl','s')

    sleep(1)

    pyautogui.press('enter')

    sleep(1)

    pyautogui.hotkey('ctrl','w')

    sleep(1)

    pyautogui.press('esc')

    sleep(1)

    if data != ultimo_valor:
        elemento_encarte = driver.find_element(By.XPATH, '//*[@id="principal"]/div/div[2]/div[1]/div[2]/div[4]')
        elemento_encarte.click()
    else:
        print('sem mais promoções')
        driver.close()


    sleep(1)


keyboard.press_and_release('windows')

sleep(1)

pyautogui.write('edge',interval=0.1)

sleep(1)

pyautogui.press('enter')

sleep(1)

keyboard.press_and_release('windows+up')

sleep(1)

pyautogui.write('https://web.whatsapp.com/',interval=0.1)

sleep(1)

pyautogui.press('enter')

sleep(10)

pyautogui.click(399,280)

sleep(1)


primeiro_arquivo = [322,157]

for a in range(0,len(data_values)):
    pyautogui.click(668,1009)

    sleep(2)

    pyautogui.click(634,701)

    sleep(2)

    pyautogui.click(primeiro_arquivo)

    sleep(2)

    pyautogui.click(776,501)

    sleep(2)

    pyautogui.click(1872,993)

    sleep(2)

    primeiro_arquivo[1] += 25


input("Deixe o navegador aberto, pressione Enter para fechar...")