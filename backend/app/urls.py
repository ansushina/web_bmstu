from django.conf.urls import url
from django.urls import path
from .views.GenreView import GenreView
from .views.GenresListView import GenresListView

urlpatterns = [
    path('genres/', GenresListView.as_view()),
    path('genres/<int:pk>/', GenreView.as_view()),
]