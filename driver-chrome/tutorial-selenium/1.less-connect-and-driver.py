from selenium import webdriver
import time


driver = webdriver.Chrome() # создание нашего браузера

url = "https://steampay.com/" #создания url для запросов

try:
    driver.get(url=url)
    time.sleep(10)
    driver.refresh()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    # закрытия нашего браузера
    driver.close()
    driver.quit()
