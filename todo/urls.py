from rest_framework.routers import DefaultRouter

from todo.views import TodoApiViewSet, DestroyAll


router = DefaultRouter()
router.register('todos', TodoApiViewSet, basename='todos')
router.register('deleteall', DestroyAll)




urlpatterns = router.urls
