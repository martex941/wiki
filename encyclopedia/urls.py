from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("no_entry", views.no_entry, name="no_entry"),
    path("<str:entry_name>", views.entry, name="entry"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit_page/<str:entry_name>/", views.edit_page, name="edit_page"),
    path("random_page/", views.random_page, name="random_page")
]
