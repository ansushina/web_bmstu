from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotAuthenticated, ParseError, NotFound, PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.UserFactory import UserFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.UserSerializer import UserSerializer

class UserView(APIView):

    @swagger_auto_schema(
        operation_summary="Returns this user information",
        responses={200: UserSerializer(),
                   401: ErrorSerializer(),
                   404: ErrorSerializer(),
                   403: ErrorSerializer()},
    )
    def get(self, request, username, format=None):
        if not request.user.is_authenticated:
            raise NotAuthenticated(detail='Please login first', code="401")
        if not request.user.username == username:
            raise PermissionDenied(detail='You can get allow only for yours information')

        usecase = UserFactory.get_user_usecase()
        user, error = usecase.get_user(username)

        if error == 'NotExist':
            raise NotFound(detail='not found')

        serializer = UserSerializer(user)
        # print(serializer.data)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update user",
        responses={200: UserSerializer(),
                   401: ErrorSerializer(),
                   404: ErrorSerializer(),
                   403: ErrorSerializer()},
        request_body=UserSerializer()
    )
    def patch(self, request, username, format=None):
        # if not request.user.is_authenticated:
        #     raise NotAuthenticated(detail='Please login first', code="401")

        if not request.user.username == username:
            raise PermissionDenied(detail='You can get allow only for yours information')
        print(request.POST.getlist("avatar"))

        if (not request.data
                or not request.data.get('email', False)):
            raise ParseError(detail="Please provide email")

        usecase = UserFactory.get_user_usecase()
        user, error = usecase.update_user(user_data={
            'email': request.data.get('email', None),
            'id': request.user.id,
            'username': username,
            # 'avatar': request.data.getlist("avatar") or None,
        })

        if error == 'NotExist':
            raise NotFound(detail='not found')

        serializer = UserSerializer(user)
        # print(serializer.data)
        return Response(serializer.data)
