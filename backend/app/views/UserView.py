from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotAuthenticated, ParseError, NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.UserFactory import UserFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.UserSerializer import UserSerializer


class UserView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary="Returns this user information",
        responses={200: UserSerializer(),
                   401: ErrorSerializer(),
                   404: ErrorSerializer()},
    )
    def get(self, request, format=None):
        if not request.user.is_authenticated:
            raise NotAuthenticated(detail='Please login first', code="401")

        usecase = UserFactory.get_user_usecase()
        user, error = usecase.get_user(request.user.id)

        if error == 'NotExist':
            raise NotFound(detail='not found')

        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create user",
        responses={200: UserSerializer(),
                   400: ErrorSerializer()},
        request_body=UserSerializer())
    def post(self, request):
        if (not request.data
                or not request.POST.get('username', False)
                or not request.POST.get('password', False)
                or not request.POST.get('email', False)):
            raise ParseError(detail="Please provide username/password/email")

        usecase = UserFactory.get_user_usecase()
        (session, error) = usecase.create_user(user_data={
            'username': request.POST['username'],
            'password': request.POST['password'],
            'email': request.POST['email']
        })

        if error == "invalid_username":
            raise ParseError(detail="invalid_username")
        elif error == "invalid_email":
            raise ParseError(detail="invalid_email")
        serializer = UserSerializer(session)
        print(serializer.data)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update user",
        responses={200: UserSerializer(),
                   401: ErrorSerializer(),
                   404: ErrorSerializer()},
        request_body=UserSerializer()
    )
    def patch(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated(detail='Please login first', code="401")

        usecase = UserFactory.get_user_usecase()
        user, error = usecase.update_user(user_data={
            'username': request.POST.get('username', None),
            'email': request.POST.get('email', None),
            'id': request.user.id,
        })

        if error == 'NotExist':
            raise NotFound(detail='not found')

        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)
