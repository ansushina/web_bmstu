from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from modules.DBRepo.CommentDBRepo import CommentDBRepo
from modules.serializers.CommentSerializer import CommentSerializer
from modules.usecases.CommentUsecases import CommentUsecases
from modules.serializers.CommentsListSerializer import CommentsListSerializer
from rest_framework.response import Response


def get_comment_usecase() -> CommentUsecases:
    return CommentUsecases(CommentDBRepo())


class CommentsListView(APIView):
    def get(self, request, film_id, format=None):
        # print(request.user.id)
        usecase = get_comment_usecase()
        comments = usecase.get_all_comments(film_id=film_id,
                                            offset=request.GET.get('offset', 0),
                                            limit=request.GET.get('limit', 10))
        print(comments)
        comments_serialiser = {
            'comments': comments
        }
        serializer = CommentsListSerializer(comments_serialiser)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, film_id, format=None):
        if not request.POST.get('text', False):
            return Response({'Error': "Please provide text"}, status="400")
        usecase = get_comment_usecase()
        comment = usecase.create_comment(film_id=film_id,
                                         user_id=request.user.id,
                                         text=request.POST['text'])
        serializer = CommentSerializer(comment)
        print(serializer.data)
        return Response(serializer.data)
