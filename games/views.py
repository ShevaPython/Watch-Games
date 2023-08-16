from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Game
from .serializer import GameListSerializer, GameDitailSerializer, ReviewCreateSerializer


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
