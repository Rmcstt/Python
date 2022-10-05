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
driver.get('https://github.com')

sleep(1)

driver.find_element(
    By.XPATH, '/html/body/div[1]/header/div/div[1]/div[1]/a').send_keys(Keys.ENTER)
sleep(1)
driver.find_element(
    By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div > div > div > a').send_keys(Keys.ENTER)
sleep(1)
driver.quit()
