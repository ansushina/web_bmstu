from rest_framework import serializers

from modules.serializers.ActorSerializer import ActorSerializer


class ActorsListSerializer(serializers.Serializer):
    actors = ActorSerializer(many=True, read_only=True)
