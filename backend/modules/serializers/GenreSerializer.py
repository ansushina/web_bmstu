from rest_framework import serializers


class GenreSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(read_only=True)


