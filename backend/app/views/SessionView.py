from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import AuthenticationFailed, ParseError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.UserFactory import UserFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.SessionSerializer import SessionSerializer
from modules.serializers.UserLoginSerializer import UserLoginSerializer


class SessionView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary="Login user",
        responses={200: SessionSerializer(),
                   400: ErrorSerializer(),
                   403: ErrorSerializer()},
        request_body=UserLoginSerializer()
    )
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, format=None):
        print(request.POST, request.data, request.data.get('username', False))
        if not request.data \
                or not request.data.get('username', False) \
                or not request.data.get('password', False):
            raise ParseError(detail="Please provide username/password")

        usecase = UserFactory.get_user_usecase()
        (session, error) = usecase.create_session(user_data={
            'username': request.data.get('username', False),
            'password': request.data.get('password', False)
        })
        print(error)
        if error == "notExist":
            raise AuthenticationFailed()

        session.token = session.token.decode()
        serialized_session = SessionSerializer(session)
        return Response(serialized_session.data)
