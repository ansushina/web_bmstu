from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from modules.DBRepo.ActorDBRepo import ActorDBRepo
from modules.usecases.ActorUsecases import ActorUsecases
from modules.serializers.ActorSerializer import ActorSerializer
from rest_framework.response import Response


def get_actor_usecase() -> ActorUsecases:
    return ActorUsecases(ActorDBRepo())


class ActorView(APIView):
    @swagger_auto_schema(responses={200: ActorSerializer()})
    def get(self, request, pk, format=None):
        usecase = get_actor_usecase()
        actor = usecase.get_actor(pk)
        serializer = ActorSerializer(actor)
        print(serializer.data)
        return Response(serializer.data)
