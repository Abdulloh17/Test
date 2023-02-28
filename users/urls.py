from django.urls import path

from .views import UserCreateApi, UserDetailApi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/users/', UserCreateApi.as_view(), name='users'),
    path('api/users/<int:pk>', UserDetailApi.as_view(), name='crud-users'),
    path('api/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='apitokin-refresh'),
]