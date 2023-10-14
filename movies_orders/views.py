from movies.models import Movie
from django.shortcuts import get_object_or_404
from .serializers import MovieOrderSerializer
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        movie_order = MovieOrderSerializer(data=request.data)

        movie_order.is_valid(raise_exception=True)

        movie_order.save(user=request.user, movie=movie)

        return Response(movie_order.data, status=status.HTTP_201_CREATED)
