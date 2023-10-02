from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView, \
    PasswordResetView, PasswordResetDoneView
from django.shortcuts import render
from django.urls import reverse_lazy

from account.forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")


class CustomPasswordResetCompleteView(PasswordResetConfirmView):
    success_url = reverse_lazy("account:password_reset_complete")


class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("account:password_reset_done")




@login_required
def profile_view(request):
    return render(request, 'account/profile.html')
