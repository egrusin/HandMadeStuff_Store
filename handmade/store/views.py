from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'store/storemask.html')


def good_page(request, good: str) -> HttpResponse:
    """Динамический URL, принимает в параметрах название товара
    Возвращает его описание, мастера, даступность из базы данных товаров"""
    return render(request, 'store/goodmask.html', {'good': good})
