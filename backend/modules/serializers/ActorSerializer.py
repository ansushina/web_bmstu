from rest_framework import serializers


class ActorSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    id = serializers.IntegerField(read_only=True)


