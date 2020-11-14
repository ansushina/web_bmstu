from rest_framework import serializers

from modules.serializers.UserSerializer import UserSerializer


class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()
    author = UserSerializer()
    film = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)