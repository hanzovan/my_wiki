from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:entry_name>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("remove", views.remove, name="remove"),
    path("rando", views.rando, name="rando")
]
