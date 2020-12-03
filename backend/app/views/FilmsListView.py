from django.http import QueryDict
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.FilmFactory import FilmFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.FilmQuerySerializer import FilmQuerySerializer
from modules.serializers.FilmSerializer import FilmSerializer


class FilmsListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns all films",
        responses={200: openapi.Response(
            description="",
            schema=openapi.Schema(type='array',
                                  items=openapi.Schema(
                                      type=openapi.TYPE_OBJECT,
                                      properties={
                                          'title': openapi.Schema(type=openapi.TYPE_STRING),
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                          'description': openapi.Schema(type=openapi.TYPE_STRING),
                                          'rating': openapi.Schema(type=openapi.TYPE_INTEGER),
                                          'year': openapi.Schema(type=openapi.TYPE_INTEGER),
                                          'created': openapi.Schema(type=openapi.TYPE_STRING,
                                                                    format=openapi.FORMAT_DATETIME),
                                          'genres': openapi.Schema(
                                              type=openapi.TYPE_OBJECT,
                                              properties={
                                                  'name': openapi.Schema(type=openapi.TYPE_STRING),
                                                  'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                              }
                                          ),
                                          'countries': openapi.Schema(
                                              type=openapi.TYPE_OBJECT,
                                              properties={
                                                  'name': openapi.Schema(type=openapi.TYPE_STRING),
                                                  'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                              }
                                          ),
                                          'actors': openapi.Schema(
                                              type=openapi.TYPE_OBJECT,
                                              properties={
                                                  'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                                                  'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                                                  'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                              }
                                          ),
                                          'image': openapi.Schema(type=openapi.TYPE_STRING,
                                                                  format=openapi.FORMAT_URI),
                                      }
                                  )
                                  )
        ),
            400: ErrorSerializer()},
        query_serializer=FilmQuerySerializer())
    def get(self, request, format=None):
        usecase = FilmFactory.get_film_usecase()
        query_params = QueryDict(query_string=self.request.GET.urlencode(), mutable=True)
        params = dict(query_params)
        # print(params)
        ser_params = FilmQuerySerializer(data=query_params)
        if not ser_params.is_valid():
            raise ParseError()
        films = usecase.get_all_films(params)
        # print(films)
        ser_films = []
        for film in films:
            ser_films.append(FilmSerializer(film).data)
        # print(serializer.data)
        return Response(ser_films)
