from rest_framework import permissions


class UserAuthPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()
