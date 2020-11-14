from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views.ActorView import ActorView
from .views.ActorsListView import ActorsListView
from .views.CountriesListView import CountriesListView
from .views.CountryView import CountryView
from .views.GenreView import GenreView
from .views.GenresListView import GenresListView
from .views.SessionView import SessionView
from .views.UserView import UserView

urlpatterns = [
    path('genres/', GenresListView.as_view()),
    path('genres/<int:pk>/', GenreView.as_view()),
    path('countries/', CountriesListView.as_view()),
    path('countries/<int:pk>/', CountryView.as_view()),
    path('actors/', ActorsListView.as_view()),
    path('actors/<int:pk>/', ActorView.as_view()),
    path('sessions/', SessionView.as_view()),
    path('users/', UserView.as_view())
]