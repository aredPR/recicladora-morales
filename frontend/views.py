from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_admin(user):    return user.is_authenticated and getattr(user, "rol", "") == "admin"
def is_operador(user): return user.is_authenticated and getattr(user, "rol", "") in ("admin", "empleado")

@login_required
def dashboard(request):     return render(request, "frontend/dashboard.html")

@login_required
@user_passes_test(is_operador)
def compras(request):       return render(request, "frontend/compras.html")

@login_required
@user_passes_test(is_operador)
def ventas(request):        return render(request, "frontend/ventas.html")

@login_required
@user_passes_test(is_operador)
def materiales(request):    return render(request, "frontend/materiales.html")

@login_required
@user_passes_test(is_operador)
def proveedores(request):   return render(request, "frontend/proveedores.html")

@login_required
@user_passes_test(is_operador)
def clientes(request):   return render(request, "frontend/clientes.html")

@login_required
@user_passes_test(is_admin)   # solo admin ve reportes si así lo decides
def reportes(request):      return render(request, "frontend/reportes.html")

@login_required
@user_passes_test(is_admin)
def configuracion(request): return render(request, "frontend/configuracion.html")
