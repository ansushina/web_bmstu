from rest_framework import serializers


class LikeSerializer(serializers.Serializer):
    value = serializers.IntegerField()
    author = serializers.IntegerField(read_only=True)
    film = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)