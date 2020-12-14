from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.ActorFactory import ActorFactory
from modules.serializers.ActorSerializer import ActorSerializer
from modules.serializers.ErrorSerializer import ErrorSerializer


class ActorView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about one actor",
        responses={200: ActorSerializer(),
                   404: ErrorSerializer()},
    )
    def get(self, request, pk, format=None):
        usecase = ActorFactory.get_actor_usecase()
        try:
            actor = usecase.get_actor(pk)
            serializer = ActorSerializer(actor)
            # print(serializer.data)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound()
