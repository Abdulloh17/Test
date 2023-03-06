from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from .models import ToDo
from .serializers import ToDoSerializer
# from rest_framework.permissions import IsAuthenticated

class TodoApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer






        