from rest_framework import permissions


class IsAdminOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        return bool(bool(request.user and request.user.is_staff))
