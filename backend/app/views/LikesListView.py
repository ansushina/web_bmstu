from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ParseError, NotAuthenticated, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.LikeFactory import LikeFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.LikeSerializer import LikeSerializer


class LikesListView(APIView):
    @swagger_auto_schema(
        operation_summary="Create like",
        responses={200: LikeSerializer(),
                   400: ErrorSerializer(),
                   401: ErrorSerializer()},
        request_body=LikeSerializer())
    def post(self, request, film_id):
        if not request.data.get('value', False) or not request.data.get('value', False) in ['1', '2', '3', '4', '5']:
            raise ParseError(detail="Please provide value")

        usecase = LikeFactory.get_like_usecase()
        like, error = usecase.create_like(film_id=film_id,
                                          user_id=request.user.id,
                                          value=request.data['value'])

        if error == 'AlreadyExist':
            raise ParseError(detail=error)
        serializer = LikeSerializer(like)
        # print(serializer.data)
        return Response(serializer.data)

    # @swagger_auto_schema(
    #     operation_summary="Returns info about like",
    #     responses={200: LikeSerializer(),
    #                404: ErrorSerializer()}, )
    # def get(self, request, film_id):
    #     if not request.user.is_authenticated:
    #         raise NotAuthenticated(detail='Please login first', code="401")
    #
    #     usecase = LikeFactory.get_like_usecase()
    #     like, error = usecase.get_like_by_user_and_film(film_id=film_id,
    #                                                     user_id=request.user.id)
    #     if error == 'NotExist':
    #         raise NotFound()
    #
    #     serializer = LikeSerializer(like)
    #     # print(serializer.data)
    #     return Response(serializer.data)
