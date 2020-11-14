from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    avatar = serializers.CharField()
    created = serializers.DateTimeField()
    id = serializers.IntegerField(read_only=True)


