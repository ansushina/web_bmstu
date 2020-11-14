from rest_framework.views import APIView

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.usecases.FilmUsecases import FilmUsecases
from modules.serializers.FilmSerializer import FilmSerializer
from rest_framework.response import Response


def get_film_usecase() -> FilmUsecases:
    return FilmUsecases(FilmDBRepo())


class FilmView(APIView):
    def get(self, request, pk, format=None):
        usecase = get_film_usecase()
        film = usecase.get_film(pk)
        serializer = FilmSerializer(film)
        print(serializer.data)
        return Response(serializer.data)

