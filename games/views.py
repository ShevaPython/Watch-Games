from django.views.generic import ListView
from .models import GameTop30TwitchStream,Game,Genre


class IndexView(ListView):
    model = GameTop30TwitchStream  # Указываем модель, с которой будем работать
    template_name = 'games/index.html'  # Указываем имя шаблона
    context_object_name = 'twitch'  # Указываем имя переменной в контексте шаблона
    paginate_by = 6  # Указываем количество объектов на странице

    def get_queryset(self):
        return GameTop30TwitchStream.objects.order_by('game')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавляем premier_matches в контекст
        context['premier_matches'] = GameTop30TwitchStream.objects.exclude(premiermatches__isnull=True)
        context['genres'] = Genre.objects.all()

        return context


class AllGamesView(ListView):
    model = Game
    template_name = 'games/games.html'
    context_object_name = 'games'
    paginate_by = 6

    def get_queryset(self):
        return Game.objects.order_by('name')