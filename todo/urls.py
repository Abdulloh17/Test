from rest_framework.routers import DefaultRouter
from django.urls import path

from todo.views import TodoApiViewSet, TodoAllDel


router = DefaultRouter()
router.register('todos', TodoApiViewSet, basename='todos')

urlpatterns = [
    path('api/todo/del/', TodoAllDel.as_view(), name='delete-all'),
]




urlpatterns += router.urls
