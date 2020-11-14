from rest_framework.response import Response
from rest_framework.views import APIView

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.DBRepo.LikeDBRepo import LikeDBRepo
from modules.serializers.LikeSerializer import LikeSerializer
from modules.usecases.LikeUsecases import LikeUsecases


def get_like_usecase() -> LikeUsecases:
    return LikeUsecases(LikeDBRepo(), FilmDBRepo())


class LikeView(APIView):
    def get(self, request, film_id, pk, format=None):
        usecase = get_like_usecase()
        like = usecase.get_like(like_id=pk)
        serializer = LikeSerializer(like)
        print(serializer.data)
        return Response(serializer.data)

    def patch(self, request, film_id, pk):
        if not request.POST.get('value', False):
            return Response({'Error': "Please provide value"}, status="400")
        usecase = get_like_usecase()
        like, error = usecase.update_like(film_id=film_id, like_id=pk, value=request.POST['value'])
        if error == 'NotExist':
            return Response({'Error': error}, status="400")
        serializer = LikeSerializer(like)
        print(serializer.data)
        return Response(serializer.data)
