from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import My_Phone,My_Password

ua = UserAgent()  # подмена юзер агента!

options = webdriver.ChromeOptions()
options.add_argument(F"user-agent={ua.random}")
driver = webdriver.Chrome(options=options)  # создание нашего браузера

url = "https://www.instagram.com/"  # создание url для запросов

try:
    driver.get(url=url)
    time.sleep(10)

    input_element_phone = driver.find_element(By.NAME, 'username')
    input_element_phone.clear()
    input_element_phone.send_keys(F'{My_Phone}')
    time.sleep(2)

    input_element_pass = driver.find_element(By.NAME,'password')
    input_element_pass.clear()
    input_element_pass.send_keys(F'{My_Password}')
    input_element_pass.send_keys(Keys.ENTER)
    time.sleep(10)



except Exception as ex:
    print(ex)
finally:
    # закрытия нашего браузера
    driver.close()
    driver.quit()

