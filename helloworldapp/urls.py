from django.urls import path
from .views import helloFunc

urlpatterns = [
    path("hello/", helloFunc),
]
