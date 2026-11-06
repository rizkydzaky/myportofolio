from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        is_editor = Group.objects.filter(
            name="Editor",
            user=request.user
        ).exists()

        return is_editor and request.method in ["PUT", "PATCH"]