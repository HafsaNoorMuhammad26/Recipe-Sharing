from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),  # Set the root view
    path("", views.recipes, name="recipes"),
]
