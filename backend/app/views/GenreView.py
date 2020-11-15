from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.GenreFactory import GenreFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.GenreSerializer import GenreSerializer


class GenreView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about one genre",
        responses={200: GenreSerializer(),
                   404: ErrorSerializer()},
    )
    def get(self, request, pk, format=None):
        usecase = GenreFactory.get_genre_usecase()
        try:
            genre = usecase.get_genre(pk)
            serializer = GenreSerializer(genre)
            print(serializer.data)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound()
