from django.db import models


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
    url = models.SlugField(max_length=100, unique=True, db_index=True, blank=True, null=True)
    peculiarities = models.ManyToManyField(Peculiarities,related_name='games',blank=True)
    photos = models.TextField(db_index=True)
    language = models.CharField("Язык", max_length=50)
    genres = models.ManyToManyField(Genre, verbose_name='жанры',related_name='game_genre')
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True,blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True,blank=True)
    video = models.TextField('Видео',blank=True,null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'




class Reviews(models.Model):
    '''Отзывы'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщения', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, null=True, blank=True)
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE,related_name='reviews')

    def __str__(self):
        return F'{self.name}-{self.game}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'