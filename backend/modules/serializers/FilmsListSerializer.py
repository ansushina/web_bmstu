from rest_framework import serializers

from modules.serializers.FilmSerializer import FilmSerializer


class FilmsListSerializer(serializers.Serializer):
    films = FilmSerializer(many=True, read_only=True)
