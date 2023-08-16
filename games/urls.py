from django.urls import path

from . import views

urlpatterns = [
    path('games/',views.GameListView.as_view()),
    path('game/<int:pk>/',views.GameDitailView.as_view()),
    path('create_review/',views.ReviewCreateView.as_view())

]