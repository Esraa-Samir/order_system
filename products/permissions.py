from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    message = "Only admins can perform this action."
    """
    A permission to check if the user is an admin.
    """

    def has_permission(self, request, view):
        return request.user.is_admin == True