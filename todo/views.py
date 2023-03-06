from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from django_filters import rest_framework as filter
from rest_framework.response import Response


from .models import ToDo
from .serializers import ToDoSerializer
from .permissions import TodoPermission

class TodoFilter(filter.FilterSet):
    class Meta:
        model = ToDo
        fields = ('user', 'title')

class TodoApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (TodoPermission, )
    filter_backends = (filter.DjangoFilterBackend, )
    filterset_class = TodoFilter
    
                    
class DestroyAll(GenericViewSet,
                 mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (TodoPermission, )

    def destroy(self, request, *args, **kwargs):
        queryset = ToDo.objects.filter(user=request.user)
        queryset = [i for i in queryset.delete()]
        return Response(status=status.HTTP_204_NO_CONTENT)





        