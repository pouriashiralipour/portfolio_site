from django.urls import path

from .views import index

app_name = "portfolio"

urlpatterns = [
    path("", index, name="portfolio_home"),
]
