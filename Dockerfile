FROM python:3.8

# Установите рабочую директорию внутри контейнера
WORKDIR /WatchGames

# Скопируйте содержимое вашего проекта в контейнер
COPY .env /WatchGames
COPY . /WatchGames

RUN pip install -r requirements.txt


# Запустите ваше приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
