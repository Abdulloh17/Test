from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from .serializers import UserSerializer, UsersDetailSerializer
from .models import User
from .permissions import UserPermission

class UserApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission, )


    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return UsersDetailSerializer
        return UserSerializer




