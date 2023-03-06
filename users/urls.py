from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserApiViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserApiViewSet, basename='users')

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='apitokin-refresh'),
]

urlpatterns += router.urls