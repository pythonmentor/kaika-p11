"""Urls for catalog"""
from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("aliment/<product_id>", views.aliment, name="aliment"),
    path("delete_favorite/<product_id>", views.delete_favorite, name="delete_favorite"),
    path("favorites/<user>", views.favorites, name="favorites"),
    path("results/<base_product>/", views.results, name="results"),
    path("save/<base_product>/<substitute_product>", views.save, name="save"),
]
