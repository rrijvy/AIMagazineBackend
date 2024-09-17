from django.urls import path
from magazine_api import views

urlpatterns = [
    path("api/", views.getData),
]
