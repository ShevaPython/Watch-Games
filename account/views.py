from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView, \
    PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from account.forms import CustomAuthenticationForm, UserRegistrationForm, UserUpdateForm
from .models import CustomUser


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")


class CustomPasswordResetCompleteView(PasswordResetConfirmView):
    success_url = reverse_lazy("account:password_reset_complete")


class CustomPasswordResetView(PasswordResetView):
    """Custom ResetView"""
    success_url = reverse_lazy("account:password_reset_done")


def register(request):
    """register User"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def update_custom_user(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST, files=request.FILES, instance=request.user)
        if user_form.is_valid():
            if 'profile_picture' in request.FILES:
                request.user.photo.delete()  # Удалить старое изображение перед обновлением
            user_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'account/update_profile.html', {'user_form': user_form})


@login_required
def profile_view(request):
    return render(request, 'account/profile.html', {'section': 'images'})


@login_required
def user_list(request):
    users = CustomUser.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(CustomUser, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})
