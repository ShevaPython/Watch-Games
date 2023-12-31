from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # url-адреса смены пароля
    path('password-change/',
         views.CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # url-адреса сброса пароля

    path("password_reset/", views.CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # register url
    path('register/', views.register, name='register'),
    path('update_profile/', views.update_custom_user, name='update_profile'),
    path('', views.profile_view, name='profile'),

    # users url
    path("users/", views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path("users/<username>/", views.user_detail, name='user_detail'),
]
