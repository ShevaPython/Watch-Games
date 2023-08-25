# https://wtools.io/ru/check-my-user-agent

from selenium import webdriver
import time
from fake_useragent import UserAgent
ua = UserAgent()#подмена юзер агента!


options = webdriver.ChromeOptions()
options.add_argument(F"user-agent={ua.random}")
driver = webdriver.Chrome(options=options) # создание нашего браузера

url = "https://wtools.io/ru/check-my-user-agent" #создания url для запросов

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
