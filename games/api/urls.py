from django.urls import path
from rest_framework import routers
from django.urls import include
from games.api.views import GameViewSet, ReviewViewSet, DeveloperViewSet, PublisherViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'developers', DeveloperViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
