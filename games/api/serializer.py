from rest_framework import serializers

from games.models import Game, Reviews, Developer, Publisher


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSwrializator(serializers.Serializer):
    """Вывод рекурсивно Children"""

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    '''Добавления отзыва'''

    class Meta:
        model = Reviews
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    ''' List отзыва'''
    children = RecursiveSwrializator(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Reviews
        fields = ('id', 'name', 'text', 'children')


class DeveloperListSerializer(serializers.ModelSerializer):
    """Вывод разработчиков"""

    class Meta:
        model = Developer
        fields = ('id', 'name')


class DeveloperDitailSerializer(serializers.ModelSerializer):
    """Вывод разработчика"""

    class Meta:
        model = Developer
        fields = '__all__'


class PublisherDitailSerializer(serializers.ModelSerializer):
    """Вывод публикантa"""

    class Meta:
        model = Publisher
        fields = '__all__'


class PublisherListSerializer(serializers.ModelSerializer):
    """Вывод публикантов"""

    class Meta:
        model = Publisher
        fields = ('id', 'name')


class GameListSerializer(serializers.ModelSerializer):
    '''Список Фильмов'''

    class Meta:
        model = Game
        fields = ('id', 'name')


class GameDitailSerializer(serializers.ModelSerializer):
    '''Детальное описания фильма'''
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    developer = GameListSerializer(read_only=True)
    publisher = PublisherListSerializer(read_only=True)
    peculiarities = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Game
        fields = '__all__'
