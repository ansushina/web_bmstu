from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.CommentFactory import CommentFactory
from modules.serializers.CommentSerializer import CommentSerializer
from modules.serializers.ErrorSerializer import ErrorSerializer


class CommentView(APIView):
    @swagger_auto_schema(
        operation_summary="Get one comment",
        responses={200: CommentSerializer(),
                   404: ErrorSerializer()})
    def get(self, request, film_id, pk, format=None):
        usecase = CommentFactory.get_comment_usecase()
        try:
            comment = usecase.get_comment(comment_id=pk)
            serializer = CommentSerializer(comment)
            # print(serializer.data)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound()

    @swagger_auto_schema(
        operation_summary="Delete comment",
        responses={200: 'ok',
                   404: ErrorSerializer(),
                   401: ErrorSerializer()})
    def delete(self, request, film_id, pk):
        usecase = CommentFactory.get_comment_usecase()
        try:
            usecase.delete_comment(comment_id=pk)
            return Response(status="200")
        except ObjectDoesNotExist:
            raise NotFound()

    @swagger_auto_schema(
        operation_summary="Update comment",
        responses={200: CommentSerializer(),
                   400: ErrorSerializer(),
                   401: ErrorSerializer(),
                   404: ErrorSerializer()},
        request_body=CommentSerializer())
    def patch(self, request, film_id, pk):
        if not request.data.get('text', False):
            raise ParseError(detail="Please provide text")

        usecase = CommentFactory.get_comment_usecase()

        try:
            comment = usecase.update_comment(comment_id=pk, text=request.data['text'])
            serializer = CommentSerializer(comment)
            # print(serializer.data)
            return Response(serializer.data)

        except ObjectDoesNotExist:
            raise NotFound()
