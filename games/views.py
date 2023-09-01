from rest_framework import generics, permissions, viewsets
from .models import Game, Developer, Publisher, Reviews
from .serializer import (GameListSerializer,
                         GameDitailSerializer,
                         ReviewCreateSerializer,
                         DeveloperListSerializer,
                         PublisherListSerializer,
                         PublisherDitailSerializer,
                         DeveloperDitailSerializer)

from .permissions import IsAdminOrIsAuthenticated


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [IsAdminOrIsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':  # Если это запрос на детали
            return GameDitailSerializer # Используем другой сериализатор
        return super().get_serializer_class()  # В противном случае используем сериализатор для списка


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
