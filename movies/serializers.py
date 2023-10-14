from rest_framework import serializers
from .models import Movie, MovieRating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    synopsis = serializers.CharField(
        allow_null=True,
        allow_blank=True,
        default='')
    rating = serializers.ChoiceField(
        choices=MovieRating.choices,
        default=MovieRating.G,
        allow_null=True,
    )
    duration = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj: Movie):
        return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
