from django.urls import path
from .views import available

urlpatterns = [
    path('rooms/', available, name="index"),
]
