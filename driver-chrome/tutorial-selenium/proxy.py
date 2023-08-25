# https://wtools.io/ru/check-my-user-agent

from selenium import webdriver
import time
from fake_useragent import UserAgent
from itertools import cycle
ua = UserAgent()#подмена юзер агента!

proxy_list = [
    "138.128.91.65:8000",
    "other_proxy_ip:port",
    # Добавьте другие прокси-серверы
]
options = webdriver.ChromeOptions()
#set proxy
proxy_cycle = cycle(proxy_list)
proxy = next(proxy_cycle)
options.add_argument(F"--proxy-server={proxy}")
driver = webdriver.Chrome(options=options) # создание нашего браузера

url = "https://whoer.net/ru" #создания url для запросов

try:
    driver.get(url=url)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    # закрытия нашего браузера
    driver.close()
    driver.quit()