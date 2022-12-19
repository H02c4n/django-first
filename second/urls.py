from django.urls import path
from .views import homesecond
urlpatterns = [
    path('', homesecond)
]
