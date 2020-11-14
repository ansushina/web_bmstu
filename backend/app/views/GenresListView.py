from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.usecases.GenreUsecases import GenreUsecases
from modules.serializers.GenresListSerializer import GenresListSerializer
from rest_framework.response import Response


def get_genre_usecase() -> GenreUsecases:
    return GenreUsecases(GenreDBRepo())


class GenresListView(APIView):
    def get(self, request, format=None):
        # print(request.user.id)
        usecase = get_genre_usecase()
        genres = usecase.get_all_genres()
        print(genres)
        genres_serialiser = {
            'genres': genres
        }
        serializer = GenresListSerializer(genres_serialiser)
        print(serializer.data)
        return Response(serializer.data)
