from django.urls import path
from .views import IndexView,AllGamesView

urlpatterns = [
  path('',IndexView.as_view(),name='index'),
  path('all_games/',AllGamesView.as_view(),name='all_games'),

]
