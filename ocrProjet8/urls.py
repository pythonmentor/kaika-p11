"""Urls for ocrProjet8 module"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("contact", views.contact, name="contact"),
    path("notice", views.legal_notice, name="notice"),
    path("search/", include("search.urls")),
]
