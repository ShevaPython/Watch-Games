from django.shortcuts import render
from .models import PremierMatches


def index(request):
    data = PremierMatches.objects.all()
    context = {'data': data}  # Создаем контекстный словарь с данными
    return render(request, 'games/index.html', context)