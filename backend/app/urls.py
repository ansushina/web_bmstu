from django.conf.urls import url
from django.urls import path

from .views.CountriesListView import CountriesListView
from .views.CountryView import CountryView
from .views.GenreView import GenreView
from .views.GenresListView import GenresListView


urlpatterns = [
    path('genres/', GenresListView.as_view()),
    path('genres/<int:pk>/', GenreView.as_view()),
    path('countries/', CountriesListView.as_view()),
    path('countries/<int:pk>/', CountryView.as_view()),
]