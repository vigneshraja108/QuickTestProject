from django.urls import path
from .views import available

urlpatterns = [
    path('rooms/', available, name="index"),
    # path('rooms/?check_in=<date>&check_out=<date>&building=,building_name>', available, name="available"),
]
