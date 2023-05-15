from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addentry/", views.add_entry, name="addentry"),
    path("edit/<str:name>", views.edit_entry, name="edit"),
    path("rand", views.rand_page, name="rand"),
    path("<str:pagename>", views.getpage, name="getpage")
]
