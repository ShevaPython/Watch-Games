FROM python:3.8

# Установите рабочую директорию внутри контейнера
WORKDIR /WatchGames

# Задать переменные среды
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Скопируйте содержимое вашего проекта в контейнер
COPY .env /WatchGames
COPY . /WatchGames
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


