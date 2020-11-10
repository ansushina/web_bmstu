from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.usecases.GenreUsecases import GenreUsecases
from modules.serializers.GenreSerializer import GenreSerializer
from rest_framework.response import Response


def get_genre_usecase() -> GenreUsecases:
    return GenreUsecases(GenreDBRepo())


class GenreView(APIView):
    def get(self, request, pk, format=None):
        usecase = get_genre_usecase()
        genre = usecase.get_genre(pk)
        serializer = GenreSerializer(genre)
        print(serializer.data)
        return Response(serializer.data)

