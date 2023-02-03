from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<a align="center" link="/store/hello">hello<a>')


def good_page(request, good: str) -> HttpResponse:
    """Динамический URL, принимает в параметрах название товара
    Возвращает его описание, мастера, даступность из базы данных товаров"""
    return HttpResponse(f'Страница товара {good}')
