from rest_framework.response import Response
from rest_framework.views import APIView

from modules.DBRepo.CommentDBRepo import CommentDBRepo
from modules.serializers.CommentSerializer import CommentSerializer
from modules.usecases.CommentUsecases import CommentUsecases


def get_comment_usecase() -> CommentUsecases:
    return CommentUsecases(CommentDBRepo())


class CommentView(APIView):
    def get(self, request, film_id, pk, format=None):
        usecase = get_comment_usecase()
        comment = usecase.get_comment(comment_id=pk)
        serializer = CommentSerializer(comment)
        print(serializer.data)
        return Response(serializer.data)

    def delete(self, request, film_id, pk):
        usecase = get_comment_usecase()
        usecase.delete_comment(comment_id=pk)
        return Response(status="200")

    def patch(self, request, film_id, pk):
        if not request.POST.get('text', False):
            return Response({'Error': "Please provide text"}, status="400")
        usecase = get_comment_usecase()
        comment = usecase.update_comment(comment_id=pk, text=request.POST['text'])
        serializer = CommentSerializer(comment)
        print(serializer.data)
        return Response(serializer.data)
