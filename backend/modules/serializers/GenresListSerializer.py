from rest_framework import serializers
from modules.serializers.GenreSerializer import GenreSerializer


class GenresListSerializer(serializers.Serializer):
    genres = GenreSerializer(many=True, read_only=True)
