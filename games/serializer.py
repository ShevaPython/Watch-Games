from rest_framework import serializers

from .models import Game, Reviews


class ReviewCreateSerializer(serializers.ModelSerializer):
    '''Добавления отзыва'''

    class Meta:
        model = Reviews
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    '''Добавления отзыва'''

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'parent')


class GameListSerializer(serializers.ModelSerializer):
    '''Список Фильмов'''

    class Meta:
        model = Game
        fields = ('name', 'description')


class GameDitailSerializer(serializers.ModelSerializer):
    '''Детальное описания фильмо'''
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    developer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    publisher = serializers.SlugRelatedField(slug_field='name', read_only=True)
    peculiarities = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Game
        exclude = ('url',)
