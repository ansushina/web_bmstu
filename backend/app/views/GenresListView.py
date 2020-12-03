from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.GenreFactory import GenreFactory
from modules.serializers.GenreSerializer import GenreSerializer
from modules.serializers.GenresListSerializer import GenresListSerializer


class GenresListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about all genres",
        responses={
            200: openapi.Response(
                description="",
                schema=openapi.Schema(type='array',
                                      items=openapi.Schema(
                                          type=openapi.TYPE_OBJECT,
                                          properties={
                                              'name': openapi.Schema(type=openapi.TYPE_STRING),
                                              'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                          }
                                      )
                                      )
            )
        }
    )
    def get(self, request, format=None):
        usecase = GenreFactory.get_genre_usecase()
        genres = usecase.get_all_genres()

        ser_genres = []
        for genre in genres:
            ser_genres.append(GenreSerializer(genre).data)
        return Response(ser_genres)
