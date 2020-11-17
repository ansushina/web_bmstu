from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.ActorFactory import ActorFactory
from modules.serializers.ActorsListSerializer import ActorsListSerializer


class ActorsListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about all actors",
        responses={200: ActorsListSerializer()}
    )
    def get(self, request, format=None):
        usecase = ActorFactory.get_actor_usecase()
        actors = usecase.get_all_actors()

        actors_serializer = {
            'actors': actors
        }
        serializer = ActorsListSerializer(actors_serializer)
        # print(serializer.data)
        return Response(serializer.data)
