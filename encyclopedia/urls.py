from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("no_entry", views.no_entry, name="no_entry"),
    path("<str:entry_name>", views.entry, name="entry")
]
