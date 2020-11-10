from abc import ABC

from rest_framework import serializers


class FilmSerialiser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    rating = serializers.IntegerField()
    genres = serializers.PrimaryKeyRelatedField(many=True)
    actors = serializers.PrimaryKeyRelatedField(many=True)
    countries = serializers.PrimaryKeyRelatedField(many=True)
    image = serializers.ImageField(allow_null=True, allow_empty_file=True)
    # comments
    created_at = serializers.DateTimeField()
