from rest_framework import permissions

class IsForecaster(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        user = request.user
        if hasattr(user, "forecaster"):
            return True
        else:
            return False