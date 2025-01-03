from django.urls import path
from .views import homePageLogic

urlpatterns = [
    path('', homePageLogic)
]