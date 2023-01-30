"""
webdriver para Safari
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Abrindo o navegador
driver = webdriver.Safari()

# Navegando para uma página
def site(url):
    return driver.get('https://'+url)


site('github.com')
user = ('coloque seu usuário aqui')
password = ('coloque sua senha aqui')
sleep(1)

driver.find_element(
    By.XPATH, '/html/body/div[1]/header/div/div[1]/div[1]/a').send_keys(Keys.ENTER)
sleep(1)

driver.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div > div > div > a').send_keys(Keys.ENTER)
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#login_field').send_keys(user)
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]').send_keys(Keys.ENTER)
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div:nth-child(7) > details > summary').send_keys(Keys.ENTER)
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div:nth-child(7) > details > details-menu > form > button').send_keys(Keys.ENTER)
sleep(2)

driver.quit()
# driver.back()
sleep(2)
# driver.quit()
