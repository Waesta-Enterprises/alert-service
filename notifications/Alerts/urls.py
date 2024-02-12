from django.urls import path, include
from .views import recieve


urlpatterns = [
    path('post/', recieve)
]