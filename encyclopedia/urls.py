from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pagename>", views.getpage, name="getpage")
]
