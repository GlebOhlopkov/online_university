from rest_framework.permissions import BasePermission


class IsOwnerYourself(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return request.method in ('PATCH',)
        return False
