from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from account.forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


@login_required
def profile_view(request):
    return render(request, 'account/profile.html')
