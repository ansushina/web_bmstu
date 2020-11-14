from rest_framework.response import Response
from rest_framework.views import APIView

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.DBRepo.LikeDBRepo import LikeDBRepo
from modules.serializers.LikeSerializer import LikeSerializer
from modules.usecases.LikeUsecases import LikeUsecases


def get_like_usecase() -> LikeUsecases:
    return LikeUsecases(LikeDBRepo(), FilmDBRepo())


class LikesListView(APIView):
    def post(self, request, film_id):
        if not request.POST.get('value', False):
            return Response({'Error': "Please provide text"}, status="400")
        usecase = get_like_usecase()
        like, error = usecase.create_like(film_id=film_id,
                                          user_id=request.user.id,
                                          value=request.POST['value'])
        if error == 'AlreadyExist':
            return Response({'Error': error}, status="400")
        serializer = LikeSerializer(like)
        print(serializer.data)
        return Response(serializer.data)

    def get(self, request, film_id):
        usecase = get_like_usecase()
        like, error = usecase.get_like_by_user_and_film(film_id=film_id,
                                                        user_id=request.user.id)
        if error == 'NotExist':
            return Response({'Error': "NotExist"}, status="400")

        serializer = LikeSerializer(like)
        print(serializer.data)
        return Response(serializer.data)
