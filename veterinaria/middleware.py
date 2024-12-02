from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class SuperuserRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        protected_urls = [
            '/', 
        ]

        if request.path in protected_urls:
            if not request.user.is_authenticated:
                print("Redirecting to login because user is not authenticated")
                return redirect('/admin/login/')  
            if not request.user.is_superuser:
                print("Forbidden access because user is not superuser")
                return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

        return self.get_response(request)
