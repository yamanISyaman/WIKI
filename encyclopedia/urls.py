from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addentry", views.add_entry, name="addentry"),
    path("<str:pagename>", views.getpage, name="getpage"),
]
