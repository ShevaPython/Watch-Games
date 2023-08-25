from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Game, Developer, Publisher
from .serializer import (GameListSerializer,
                         GameDitailSerializer,
                         ReviewCreateSerializer,
                         DeveloperListSerializer,
                         PublisherListSerializer,
                         PublisherDitailSerializer,
                         DeveloperDitailSerializer)


class GameListView(APIView):
    """Вывод списков фильмов"""

    def get(self, request):
        games = Game.objects.all()
        serialiser = GameListSerializer(games, many=True)
        return Response(serialiser.data)


class GameDitailView(APIView):
    """Полное описанние фильмов"""

    def get(self, request, pk):
        game = Game.objects.get(id=pk)
        serialiser = GameDitailSerializer(game)
        return Response(serialiser.data)


class ReviewCreateView(APIView):
    """Добавления коментапия к Игре"""

    def post(self, request):
        rewiew = ReviewCreateSerializer(data=request.data)
        if rewiew.is_valid():
            rewiew.save()
        return Response(status=201)


class DeveloperListView(generics.ListAPIView):
    """Вывод разработчиков"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperListSerializer


class PublisherListView(generics.ListAPIView):
    """Вывод публикантов"""
    queryset = Publisher.objects.all()
    serializer_class = PublisherListSerializer


class DeveloperDetailListView(generics.RetrieveAPIView):
    """Вывод разработчика"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperDitailSerializer


class PublisherDetailListView(generics.RetrieveAPIView):
    """Вывод публиканта"""
    queryset = Developer.objects.all()
    serializer_class = PublisherDitailSerializer
