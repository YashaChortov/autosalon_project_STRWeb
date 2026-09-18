from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def employee_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:login')
        # Пускаем и сотрудников, и суперпользователя
        if not (request.user.is_employee or request.user.is_superuser):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper