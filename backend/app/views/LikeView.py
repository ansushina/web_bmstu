from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.LikeFactory import LikeFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.LikeSerializer import LikeSerializer


class LikeView(APIView):
    @swagger_auto_schema(
        operation_summary="returns info about like",
        responses={200: LikeSerializer(),
                   404: ErrorSerializer()})
    def get(self, request, film_id, pk, format=None):
        usecase = LikeFactory.get_like_usecase()
        try:
            like = usecase.get_like(like_id=pk)
            serializer = LikeSerializer(like)
            print(serializer.data)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound()

    @swagger_auto_schema(
        operation_summary="Update like",
        responses={200: LikeSerializer(),
                   400: ErrorSerializer(),
                   404: ErrorSerializer(),
                   401: ErrorSerializer()},
        request_body=LikeSerializer())
    def patch(self, request, film_id, pk):
        if not request.POST.get('value', False):
            raise ParseError(detail="Please provide value")
        usecase = LikeFactory.get_like_usecase()
        like, error = usecase.update_like(film_id=film_id, like_id=pk, value=request.POST['value'])
        if error == 'NotExist':
            return NotFound()
        serializer = LikeSerializer(like)
        print(serializer.data)
        return Response(serializer.data)
