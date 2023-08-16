from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Открываем браузер и загружаем страницу
driver = webdriver.Chrome()  # Используйте Chrome или другой драйвер, в зависимости от вашего браузера
url = "https://steampay.com/action"  # Замените на URL нужной страницы
driver.get(url)

# Прокручиваем страницу для загрузки всех данных
scroll_pause_time = 5  # Задержка в секундах между прокрутками
scroll_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height

# Получаем исходный код страницы с динамически загруженными данными
page_source = driver.page_source

# Закрываем браузер
driver.quit()

# Сохраняем исходный код страницы в файл
with open("page_code.html", "w", encoding="utf-8") as file:
    file.write(page_source)

# Считываем исходный код страницы из файла
with open("page_code.html", "r", encoding="utf-8") as file:
    page_source = file.read()

# Работаем с исходным кодом страницы с помощью BeautifulSoup для извлечения данных
soup = BeautifulSoup(page_source, 'html.parser')
# Используйте методы BeautifulSoup для поиска и извлечения нужных данных
