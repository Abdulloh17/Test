from rest_framework.permissions import BasePermission


class TodoPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user.pk == request.user.pk)