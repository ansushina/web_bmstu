from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.DBRepo.UserDBRepo import UserDBRepo
from modules.usecases.GenreUsecases import GenreUsecases
from modules.serializers.GenreSerializer import GenreSerializer
from rest_framework.response import Response

from modules.usecases.UserUsecases import UserUsecases


def get_user_usecase() -> UserUsecases:
    return UserUsecases(UserDBRepo())




class SessionView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")

        usecase = get_user_usecase()
        (session, error) = usecase.create_session(user_data={
            'username': request.POST['username'],
            'password': request.POST['password']
        })
        if error == "user_not_exist" :
            return Response({'Error': "UserNotExist"}, status="400")
        return Response({'username': session.username, 'token': session.token})


