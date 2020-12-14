from typing import List

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.entities.Actor import Actor
from modules.factories.ActorFactory import ActorFactory
from modules.serializers.ActorSerializer import ActorSerializer


class ActorsListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about all actors",
        responses={200: openapi.Response(
            description="",
            schema=openapi.Schema(type='array',
                                  items=openapi.Schema(
                                      type=openapi.TYPE_OBJECT,
                                      properties={
                                          'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                                          'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                                          'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                      }
                                  )))
        }
    )
    def get(self, request, format=None):
        usecase = ActorFactory.get_actor_usecase()
        actors = usecase.get_all_actors()

        ser_actors = []
        for actor in actors:
            ser_actors.append(ActorSerializer(actor).data)
        # print(serializer.data)
        return Response(ser_actors)
