from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django_filters import rest_framework as filter


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
    
                    
    





        