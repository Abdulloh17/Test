from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from .serializers import UserSerializer, UsersDetailSerializer, UserRegisterSerializer
from .models import User


class UserApiViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer



    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return UsersDetailSerializer
        if self.action in ('create',):
            return UserRegisterSerializer
        return UserSerializer




