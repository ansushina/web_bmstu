from abc import ABC

from rest_framework import serializers

from modules.serializers.ActorSerializer import ActorSerializer
from modules.serializers.CountrySerializer import CountrySerializer
from modules.serializers.GenreSerializer import GenreSerializer


class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    rating = serializers.IntegerField()
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    countries = CountrySerializer(many=True)
    image = serializers.ImageField(allow_null=True, allow_empty_file=True)
    created = serializers.DateTimeField()
