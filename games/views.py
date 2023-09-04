from rest_framework import viewsets
from .models import Game, Developer, Publisher, Reviews
from .serializer import (GameListSerializer,
                         GameDitailSerializer,
                         ReviewCreateSerializer,
                         DeveloperListSerializer,
                         PublisherListSerializer,
                         PublisherDitailSerializer,
                         DeveloperDitailSerializer,
                         ReviewSerializer)

from .permissions import IsAdminOrIsAuthenticated


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [IsAdminOrIsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':  # Если это запрос на детали
            return GameDitailSerializer  # Используем другой сериализатор
        return super().get_serializer_class()  # В противном случае используем сериализатор для списка


class ReviewViewSet(viewsets.ModelViewSet):
    """Отзывы"""
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrIsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return super().get_serializer_class()


class DeveloperViewSet(viewsets.ModelViewSet):
    """Разработчики"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperListSerializer
    permission_classes = [IsAdminOrIsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DeveloperDitailSerializer
        return super().get_serializer_class()


class PublisherViewSet(viewsets.ModelViewSet):
    """Издатели"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PublisherDitailSerializer
        return super().get_serializer_class()
