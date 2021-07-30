from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('obras', views.BooksListView.as_view(), name="obras"),
    path('autores', views.AuthorsListView.as_view(), name="autores"),
]