from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.GenreFactory import GenreFactory
from modules.serializers.GenresListSerializer import GenresListSerializer


class GenresListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about all genres",
        responses={200: GenresListSerializer(), },
    )
    def get(self, request, format=None):
        usecase = GenreFactory.get_genre_usecase()
        genres = usecase.get_all_genres()

        genres_serialiser = {
            'genres': genres
        }
        serializer = GenresListSerializer(genres_serialiser)
        print(serializer.data)
        return Response(serializer.data)
