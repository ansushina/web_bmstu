from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views.ActorView import ActorView
from .views.ActorsListView import ActorsListView
from .views.CommentView import CommentView
from .views.CommentsListView import CommentsListView
from .views.CountriesListView import CountriesListView
from .views.CountryView import CountryView
from .views.FilmView import FilmView
from .views.FilmsListView import FilmsListView
from .views.GenreView import GenreView
from .views.GenresListView import GenresListView
from .views.LikeView import LikeView
from .views.LikesListView import LikesListView
from .views.SessionView import SessionView
from .views.UserView import UserView
from .views.UsersListView import UsersListView

urlpatterns = [
    path('genres/', GenresListView.as_view()),
    path('genres/<int:pk>/', GenreView.as_view()),
    path('countries/', CountriesListView.as_view()),
    path('countries/<int:pk>/', CountryView.as_view()),
    path('actors/', ActorsListView.as_view()),
    path('actors/<int:pk>/', ActorView.as_view()),
    path('sessions/', SessionView.as_view()),
    path('users/', UsersListView.as_view()),
    path('users/<slug:username>/', UserView.as_view()),
    path('films/<int:pk>/', FilmView.as_view()),
    path('films/', FilmsListView.as_view()),
    path('films/<int:film_id>/comments/', CommentsListView.as_view()),
    path('films/<int:film_id>/comments/<int:pk>/', CommentView.as_view()),
    path('films/<int:film_id>/likes/', LikesListView.as_view()),
    path('films/<int:film_id>/likes/<slug:username>/', LikeView.as_view()),
]