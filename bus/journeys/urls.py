from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:journey_id>", views.journey, name="journey"),
    path("<int:journey_id>/book", views.book, name="book")
]
