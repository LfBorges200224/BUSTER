from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from .serializers import MovieSerializer
from rest_framework.pagination import PageNumberPagination
from users.permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Movie
from django.http import Http404


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movies_obj = Movie.objects.all()

        result_page = self.paginate_queryset(movies_obj, request)

        movies = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(movies.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
        print(movie)

        return Response(MovieSerializer(movie).data, status=status.HTTP_200_OK)
