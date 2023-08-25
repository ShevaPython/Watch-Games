import json
import time
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver

ua = UserAgent()  # Подмена юзер агента!

options = webdriver.ChromeOptions()
options.add_argument(F"user-agent={ua.random}")
driver = webdriver.Chrome(options=options)  # Создание нашего браузера
url = {
    "url_action": "https://steampay.com/action",
    "url_adventure": "https://steampay.com/adventure",
    "url_rpg": "https://steampay.com/rpg",
    "url_simulation": "https://steampay.com/simulation",
    "url_strategy": "https://steampay.com/strategy",
    "url_sports":"https://steampay.com/sports",
    "url_racing":"https://steampay.com/racing",
    "url_casual":"https://steampay.com/casual"
}
def pars_url(url_dict):
    try:
        for category, url in url_dict.items():
            driver.get(url=url)
            time.sleep(10)
            elements_action = driver.find_elements(By.CLASS_NAME, "catalog-item")

            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # прокрутка вниз!
                time.sleep(2)  # Подождем, чтобы новые элементы подгрузились
                new_elements = driver.find_elements(By.CLASS_NAME, "catalog-item")

                if len(new_elements) == len(elements_action):
                    break  # Если больше нет новых элементов, выходим из цикла

                elements_action = new_elements

            urls = []  # Список для хранения URL-адресов

            for element in elements_action:
                url = element.get_attribute("href")  # Получение атрибута href из ссылки
                if url:
                    urls.append(url)  # Добавление URL в список

            print(f"Category: {category}")
            print("Number of elements:", len(elements_action))
            print("Number of URLs:", len(urls))
            print("URLs:", urls)

            # Сохранение URL-адресов в JSON файл
            with open(f"urls_{category}.json", "w") as f:
                json.dump(urls, f, indent=4)

            time.sleep(15)
    except Exception as ex:
        print(ex)
    finally:
        # Закрытие нашего браузера
        driver.close()
        driver.quit()


if __name__ == "__main__":
    pars_url(url_dict=url)



