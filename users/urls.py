from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveUpdateAPIView, UserDestroyAPIView

urlpatterns = [

    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user-detail'),
    path('users/<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]