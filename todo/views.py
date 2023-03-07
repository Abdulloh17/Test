from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import generics



from .models import ToDo
from .serializers import ToDoSerializer
from .permissions import TodoPermission


class TodoApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (TodoPermission, )
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')


    
                    
class TodoAllDel(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (TodoPermission, )


    def delete(self, request, *args, **kwargs):
        todo = ToDo.objects.filter(user = request.user)
        todo = [i for i in todo.delete()]

        return Response({'delete': 'Все таски удалены'})





        