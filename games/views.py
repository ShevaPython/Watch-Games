from rest_framework import generics,permissions
from .models import Game, Developer, Publisher, Reviews
from .serializer import (GameListSerializer,
                         GameDitailSerializer,
                         ReviewCreateSerializer,
                         DeveloperListSerializer,
                         PublisherListSerializer,
                         PublisherDitailSerializer,
                         DeveloperDitailSerializer)


class GameListView(generics.ListAPIView):
    """Вывод списков фильмов"""

    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [permissions.IsAuthenticated]


class GameDitailView(generics.RetrieveAPIView):
    """Полное описанние фильмов"""
    queryset = Game.objects.all()
    serializer_class = GameDitailSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]


class ReviewCreateView(generics.ListCreateAPIView):
    """Добавления коментапия к Игре"""
    queryset = Reviews.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewListView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = PublisherListSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeveloperListView(generics.ListAPIView):
    """Вывод разработчиков"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperListSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublisherListView(generics.ListAPIView):
    """Вывод публикантов"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherListSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeveloperDetailListView(generics.RetrieveAPIView):
    """Вывод разработчика"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperDitailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublisherDetailListView(generics.RetrieveAPIView):
    """Вывод публиканта"""
    queryset = Developer.objects.all()
    serializer_class = PublisherDitailSerializer
    permission_classes = [permissions.IsAuthenticated]
