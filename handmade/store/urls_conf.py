from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('<good>/', good_page),
]