from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import GameViewSet,Reviews

router = routers.DefaultRouter()
router.register(r'games',GameViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('create_review/', views.ReviewCreateView.as_view()),
    # path('review/',views.ReviewListView.as_view()),
    # path('developers/', views.DeveloperListView.as_view()),
    # path('publishers/', views.PublisherListView.as_view()),
    # path('developer/<int:pk>/', views.DeveloperDetailListView.as_view()),
    # path('publisher/<int:pk>/', views.PublisherDetailListView.as_view()),

]
