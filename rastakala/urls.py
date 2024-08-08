from django.urls import path, re_path

from . import views

app_name = "rastakala"

urlpatterns = [path("", views.index, name="home_page")]
