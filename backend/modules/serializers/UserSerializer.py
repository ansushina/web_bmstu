from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    avatar = serializers.CharField(required=False)
    created = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)


