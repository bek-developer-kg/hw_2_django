from django.urls import path
from main.views import main ,mix

urlpatterns = [
    path('main/', main, name='main'),
    path('mix/', mix, name='mix')
]
