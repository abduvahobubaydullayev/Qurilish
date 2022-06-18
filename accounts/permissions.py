from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print('********')
        print(request.user)
        print(obj.username)
        print('***********')
        print(type(obj.username), type(request.user))
        return str(obj.username) == str(request.user)


class IsNotOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('********')
        print(request.user)
        print(obj.username)
        print('***********')
        if request.method in permissions.SAFE_METHODS:
            return False

        return str(obj.username) != str(request.user)
