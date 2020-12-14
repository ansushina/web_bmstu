from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.CommentFactory import CommentFactory
from modules.serializers.CommentQuerySerializer import CommentQuerySerializer
from modules.serializers.CommentSerializer import CommentSerializer
from modules.serializers.CommentsListSerializer import CommentsListSerializer
from modules.serializers.ErrorSerializer import ErrorSerializer


class CommentsListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns all film comments",
        responses={200: openapi.Response(
                description="",
                schema=openapi.Schema(type='array',
                                      items=openapi.Schema(
                                          type=openapi.TYPE_OBJECT,
                                          properties={
                                              'text': openapi.Schema(type=openapi.TYPE_STRING),
                                              'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                          }
                                      )
                                      )
            ),
                   400: ErrorSerializer()},
        query_serializer=CommentQuerySerializer())
    def get(self, request, film_id, format=None):

        ser_query = CommentQuerySerializer(data=request.GET)
        if not ser_query.is_valid():
            return ParseError()

        usecase = CommentFactory.get_comment_usecase()
        comments = usecase.get_all_comments(film_id=film_id,
                                            offset=request.GET.get('offset', 0),
                                            limit=request.GET.get('limit', 10))
        # print(comments)
        ser_comments = []
        for comment in comments:
            ser_comments.append(CommentSerializer(comment).data)
        # print(serializer.data)
        return Response(ser_comments)

    @swagger_auto_schema(
        operation_summary="Create comment",
        responses={200: CommentSerializer(),
                   400: ErrorSerializer(),
                   401: ErrorSerializer()},
        request_body=CommentSerializer())
    def post(self, request, film_id, format=None):
        if not request.data.get('text', False):
            raise ParseError(detail="Please provide text")
        usecase = CommentFactory.get_comment_usecase()
        comment = usecase.create_comment(film_id=film_id,
                                         user_id=request.user.id,
                                         text=request.data['text'])
        serializer = CommentSerializer(comment)
        # print(serializer.data)
        return Response(serializer.data)
