from django.urls import path, include
from .views import fetch


urlpatterns = [
    path('fetch/', fetch)
]