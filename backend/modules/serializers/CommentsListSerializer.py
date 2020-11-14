from rest_framework import serializers

from modules.serializers.CommentSerializer import CommentSerializer
from modules.serializers.GenreSerializer import GenreSerializer


class CommentsListSerializer(serializers.Serializer):
    comments = CommentSerializer(many=True, read_only=True)
