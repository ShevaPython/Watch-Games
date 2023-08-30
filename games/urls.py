from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.GameListView.as_view()),
    path('game/<int:pk>/', views.GameDitailView.as_view()),
    path('create_review/', views.ReviewCreateView.as_view()),
    path('review/',views.ReviewListView.as_view()),
    path('developers/', views.DeveloperListView.as_view()),
    path('publishers/', views.PublisherListView.as_view()),
    path('developer/<int:pk>/', views.DeveloperDetailListView.as_view()),
    path('publisher/<int:pk>/', views.PublisherDetailListView.as_view()),

]
