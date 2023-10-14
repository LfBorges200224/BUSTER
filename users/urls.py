from django.urls import path
from .views import UserView, UserDetailView, CustomTokenObtainPairSerializer


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", CustomTokenObtainPairSerializer.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
