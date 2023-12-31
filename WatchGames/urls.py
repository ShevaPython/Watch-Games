"""
URL configuration for WatchGames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from games.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('games.api.urls')),
    # index main
    path('', include('games.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    # auth
    path('account/', include('account.urls', namespace='account')),
    path('social-auth/',
         include('social_django.urls', namespace='social')),
    # images
    path('images/', include('images.urls', namespace='images')),
    # shop
    path('payment/', include('payment.urls', namespace='payment')),
    path('shop/', include('shop.url', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),


    #debug_toolbar
    path('__debug__/', include('debug_toolbar.urls')),

]

urlpatterns += doc_urls
if settings.DEBUG:
    import mimetypes

    mimetypes.add_type('webhooks/javascript', '.js', True)
    mimetypes.add_type('text/css', '.css', True)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
