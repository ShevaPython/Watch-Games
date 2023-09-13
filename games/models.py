from django.db import models
from transliterate import translit

from games.service import generate_random_string


class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Жанр', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publisher(models.Model):
    """Издатель"""
    name = models.CharField('Издатель', max_length=100, db_index=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Developer(models.Model):
    """Разработчик"""
    name = models.CharField('Разработчик', max_length=100, db_index=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class Peculiarities(models.Model):
    name = models.CharField('Особенности', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'


class Game(models.Model):
    """Игра"""
    name = models.CharField('Игра', max_length=100, db_index=True)
    description = models.TextField('Описание')
    peculiarities = models.ManyToManyField(Peculiarities, related_name='games', blank=True)
    photos = models.TextField(db_index=True)
    language = models.CharField("Язык", max_length=50, null=True, blank=True)
    genres = models.ManyToManyField(Genre, verbose_name='жанры', related_name='game_genre')
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    data_create = models.CharField(max_length=100,verbose_name='Дата выхода',default='absent')

    def __str__(self):
        return self.name or ''

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Reviews(models.Model):
    '''Отзывы'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщения', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='children')
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return F'{self.name}-{self.game}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class GameTop30TwitchStream(models.Model):
    game = models.CharField(max_length=100, verbose_name='Название стрима')
    href = models.TextField()
    photo = models.TextField(db_index=True,
                             default='https://w.forfun.com/fetch/f5/f53d0a93243e09cb47b41dac9d46a42e.jpeg')
    premiermatches = models.TextField(blank=True, null=True)

    def __str__(self):
        return F"{self.game}" or ""
