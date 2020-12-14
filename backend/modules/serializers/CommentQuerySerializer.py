from rest_framework import serializers


class CommentQuerySerializer(serializers.Serializer):
        offset = serializers.IntegerField(required=False)
        limit = serializers.IntegerField(required=False)