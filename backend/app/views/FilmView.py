from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.factories.FilmFactory import FilmFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.usecases.FilmUsecases import FilmUsecases
from modules.serializers.FilmSerializer import FilmSerializer
from rest_framework.response import Response


class FilmView(APIView):
    @swagger_auto_schema(
        operation_summary="Get one film",
        responses={200: FilmSerializer(),
                   404: ErrorSerializer()})
    def get(self, request, pk, format=None):
        usecase = FilmFactory.get_film_usecase()
        try:
            film = usecase.get_film(pk)
            serializer = FilmSerializer(film)
            # print(serializer.data)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound()

