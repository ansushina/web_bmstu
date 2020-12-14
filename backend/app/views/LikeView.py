from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound, ParseError, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.LikeFactory import LikeFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.LikeSerializer import LikeSerializer


class LikeView(APIView):
    @swagger_auto_schema(
        operation_summary="returns info about like",
        responses={200: LikeSerializer(),
                   404: ErrorSerializer(),
                   403: ErrorSerializer()})
    def get(self, request, film_id, username, format=None):
        print(username, request.user.username)
        if not username == request.user.username:
            raise PermissionDenied(detail='You can get allow only for yours information')
        usecase = LikeFactory.get_like_usecase()

        print('here')
        (like, error) = usecase.get_like_by_user_and_film(username=username, film_id=film_id)
        if error:
            raise NotFound()
        serializer = LikeSerializer(like)
        print(serializer.data)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update like",
        responses={200: LikeSerializer(),
                   400: ErrorSerializer(),
                   404: ErrorSerializer(),
                   401: ErrorSerializer(),
                   403: ErrorSerializer()},
        request_body=LikeSerializer())
    def patch(self, request, film_id, username):
        if not username == request.user.username:
            return PermissionDenied(detail='You can get allow only for yours information')
        if not request.data.get('value', False) or not request.data.get('value', False) in ['1', '2', '3', '4', '5']:
            raise ParseError(detail="Please provide value from 1 to 5")
        usecase = LikeFactory.get_like_usecase()
        like, error = usecase.update_like_by_user_and_film(film_id=film_id, username=username,
                                                           value=request.data['value'])
        if error == 'NotExist':
            raise NotFound()
        serializer = LikeSerializer(like)
        # print(serializer.data)
        return Response(serializer.data)

    def delete(self, request, film_id, username):
        usecase = LikeFactory.get_like_usecase()
        try:
            usecase.delete_like(film_id=film_id, username=username)
            return Response(status="200")
        except ObjectDoesNotExist:
            raise NotFound()
