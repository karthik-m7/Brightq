from django.shortcuts import redirect
from django.urls import path, re_path

from website import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="index"),
    ]