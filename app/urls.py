from django.urls import path
from . import views

urlpatterns = [
    path("page", views.frontpage, name="page"),
    path("", views.sidebar, name="sidebar")
]