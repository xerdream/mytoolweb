from django.urls import path

from . import views

app_name = "m3u8"
urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),
    path("download/", views.download, name="download"),
]
