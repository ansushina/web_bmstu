from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from modules.DBRepo.ActorDBRepo import ActorDBRepo
from modules.usecases.ActorUsecases import ActorUsecases
from modules.serializers.ActorsListSerializer import ActorsListSerializer
from rest_framework.response import Response


def get_actor_usecase() -> ActorUsecases:
    return ActorUsecases(ActorDBRepo())


class ActorsListView(APIView):
    def get(self, request, format=None):
        usecase = get_actor_usecase()
        actors = usecase.get_all_actors()
        print(actors)
        actors_serializer = {
            'actors': actors
        }
        serializer = ActorsListSerializer(actors_serializer)
        print(serializer.data)
        return Response(serializer.data)

