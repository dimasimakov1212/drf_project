from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    """
    Задаем права пользователей
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        if request.user == view.get_object.owner:
            return True
