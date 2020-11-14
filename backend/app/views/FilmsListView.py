from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.serializers.FilmsListSerializer import FilmsListSerializer
from modules.usecases.FilmUsecases import FilmUsecases


def get_film_usecase() -> FilmUsecases:
    return FilmUsecases(FilmDBRepo())


class FilmsListView(APIView):
    def get(self, request, format=None):
        usecase = get_film_usecase()
        query_params = QueryDict(query_string=self.request.GET.urlencode(), mutable=True)
        params = dict(query_params)
        print(params)
        films = usecase.get_all_films(params)
        print(films)
        films_serialiser = {
            'films': films
        }
        serializer = FilmsListSerializer(films_serialiser)
        print(serializer.data)
        return Response(serializer.data)
