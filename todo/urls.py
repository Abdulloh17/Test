from rest_framework.routers import DefaultRouter

from todo.views import TodoApiViewSet


router = DefaultRouter()
router.register('todos', TodoApiViewSet, basename='todos')


# urlpatterns = [
#     path('api/todos/', TodoCreateApi.as_view(), name='todos'),
#     path('api/todos/<int:pk>', ToDoDetailApi.as_view(), name='crud-todo'),
# ]

urlpatterns = router.urls
