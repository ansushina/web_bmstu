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
    def get(self, request, film_id, user_id, format=None):
        if not user_id == request.user.id:
            return PermissionDenied(detail='You can get allow only for yours information')
        usecase = LikeFactory.get_like_usecase()
        try:
            like = usecase.get_like_by_user_and_film(film_id=film_id, user_id=user_id)
            serializer = LikeSerializer(like)
            # print(serializer.data)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound()

    @swagger_auto_schema(
        operation_summary="Update like",
        responses={200: LikeSerializer(),
                   400: ErrorSerializer(),
                   404: ErrorSerializer(),
                   401: ErrorSerializer(),
                   403: ErrorSerializer()},
        request_body=LikeSerializer())
    def patch(self, request, film_id, user_id):
        if not user_id == request.user.id:
            return PermissionDenied(detail='You can get allow only for yours information')
        if not request.POST.get('value', False):
            raise ParseError(detail="Please provide value")
        usecase = LikeFactory.get_like_usecase()
        like, error = usecase.get_like_by_user_and_film(film_id=film_id, user_id=user_id, value=request.POST['value'])
        if error == 'NotExist':
            return NotFound()
        serializer = LikeSerializer(like)
        # print(serializer.data)
        return Response(serializer.data)
