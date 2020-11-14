from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from modules.DBRepo.UserDBRepo import UserDBRepo
from modules.entities.User import User
from modules.usecases.UserUsecases import UserUsecases
from modules.serializers.UserSerializer import UserSerializer
from rest_framework.response import Response


def get_user_usecase() -> UserUsecases:
    return UserUsecases(UserDBRepo())


class UserView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(responses={200: UserSerializer()})
    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({'Error': "Please login first"}, status="400")
        usecase = get_user_usecase()
        user = usecase.get_user(request.user.id)
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide username/password/email"}, status="400")

        usecase = get_user_usecase()
        (session, error) = usecase.create_user(user_data={
            'username': request.POST['username'],
            'password': request.POST['password'],
            'email': request.POST['email']
        })

        if error == "invalid_username":
            return Response({'Error': "invalid_username"}, status="400")
        elif error == "invalid email":
            return Response({'Error': "invalid_email"}, status="400")
        serializer = UserSerializer(session)
        print(serializer.data)
        return Response(serializer.data)