from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from modules.factories.UserFactory import UserFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.UserSerializer import UserSerializer


class UsersListView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary="Create user",
        responses={200: UserSerializer(),
                   400: ErrorSerializer()},
        request_body=UserSerializer())
    def post(self, request):
        if (not request.data
                or not request.data.get('username', False)
                or not request.data.get('password', False)
                or not request.data.get('email', False)):
            raise ParseError(detail="Please provide username/password/email")

        usecase = UserFactory.get_user_usecase()
        (session, error) = usecase.create_user(user_data={
            'username': request.data['username'],
            'password': request.data['password'],
            'email': request.data['email']
        })

        if error == "invalid_username":
            raise ParseError(detail="invalid_username")
        elif error == "invalid_email":
            raise ParseError(detail="invalid_email")
        serializer = UserSerializer(session)
        print(serializer.data)
        return Response(serializer.data)