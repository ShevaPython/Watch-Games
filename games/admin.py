from django.contrib import admin

from .models import Genre, Game, Developer, Publisher, Peculiarities, Reviews, GameTop30TwitchStream


@admin.register(GameTop30TwitchStream)
class GameTop100Admin(admin.ModelAdmin):
    pass



@admin.register(Peculiarities)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass
