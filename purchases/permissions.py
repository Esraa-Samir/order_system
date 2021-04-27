from rest_framework import permissions
from products.models import Product


class IsNotAdmin(permissions.BasePermission):
    message = "An admin can not perform this action."
    """
        A permission to check that a user is a normal user.
    """

    def has_permission(self, request, view):
        return request.user.is_admin == False


class IsAdmin(permissions.BasePermission):
    message = "Only admins can perform this action."
    """
        A permission to check if the user is an admin.
    """

    def has_permission(self, request, obj):
        return request.user.is_admin == True


class IsAvailable(permissions.BasePermission):
    message = "Product is not available."
    """
        A permission to check if a product ia available.
    """

    def has_permission(self, request, obj):
        available_products = Product.objects.filter(is_available=True).values_list('id',flat=True)
        return int(request.data['item']) in available_products


class IsNotOwner(permissions.BasePermission):
    message = "Product owners' can not purchase their product."
    """
        A permission to check if the user owe a product.
    """

    def has_permission(self, request, obj):
        products = Product.objects.filter(owner_id=request.user.id).values_list('id',flat=True)
        return not (int(request.data['item']) in products)