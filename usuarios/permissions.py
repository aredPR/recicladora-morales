from rest_framework.permissions import BasePermission

class IsAdminOrReadCreateOnly(BasePermission):
    """
    Admin: acceso total (GET/POST/PATCH/PUT/DELETE).
    Operador (empleado): solo lectura y creación (GET/HEAD/OPTIONS/POST).
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # Admin: todo permitido
        if getattr(user, "rol", "") == "admin":
            return True

        # Operador/empleado: solo GET/HEAD/OPTIONS/POST
        return request.method in ("GET", "HEAD", "OPTIONS", "POST")
